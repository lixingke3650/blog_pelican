Skills Summary
################

:title: Skills Summary
:date: 2014-07-22 22:00
:category: 整理
:tags:
:author: Hanbin

总结小的技巧，经验。

-------

大数据处理软件Hadoop印象
========================
  
Hadoop是Apache对谷歌google　File　System与MapReduce的实现，  
主要包含了NDFS与MapReduce。  
NDFS是存储海量数据的文件系统，包含容错，分布式存储等特性；    
MapReduce是一种从海量数据中分析提取最后结果的一个模型。  
  
----

网站攻击方式　XSS和CSRF
=========================
  
XSS(cross site scripting)，在网页中注入脚本的方式实现攻击。  
CSRF(Cross-site request forgery)，伪造用户cookie的攻击方式。  
  
2015-04-16  
  
------

Linux身份验证模块-PAM  
=========================
  
配置vsftp的虚拟账户，发现需要PAM来协助完成身份验证，  
PAM利用一系列链接库实现各种不同的认证及管理方式。  
其他应用可通过配置文件和API函数来借助PAM完成认证。  
PAM包含了账号管理，认证管理，密码管理，会话管理服务。  
  
2015-04-10  
  
------

PostgreSQL增强工具-pgpool-II
=================================
  
pgpool是工作在PostgreSQL与客户端之间的一个中间件。  
提供了一些诱人的功能：  

* 连接池　　　　　　　为客户端保持连接，可重用相同参数的连接，减小连接开销  
* 备份　　　　　　　　　可管理多个PostgreSQL数据库，并同步数据，其中一个数据库坏掉可不影响服务  
* 负载均衡　　　　　　管理多个PostgreSQL数据库时，可分散SELECT，减少单台数据库压力  
* 优化的并行查询　　可将并行查询分散到不同服务器，提高查询速度减少单台压力　　
　　
2014-10-11  
  
------

PostgreSQL获取表字段名及定义
==================================
  
背景
----

在做跨库表复制时，需要将表的定义信息告知INSERT INTO函数，否则复制失败。  
以下函数用来获取指定表的字段名及其定义。  
  
实现
----

.. code-block:: PlPgsql

    CREATE OR REPLACE FUNCTION get_columndef(regclass)
      RETURNS text AS
    $BODY$

    BEGIN
        RETURN (SELECT array_to_string(array_agg(f), ',') 
                  FROM (SELECT quote_ident(attname) || ' ' || format_type(atttypid, atttypmod) AS f
                          FROM pg_attribute
                         WHERE attrelid = $1
                               AND attnum > 0
                               AND NOT attisdropped
                         ORDER BY attnum) t);

    EXCEPTION 
        WHEN QUERY_CANCELED THEN
            PERFORM * FROM "log_err"(...);
            RETURN '';
        WHEN OTHERS THEN
            PERFORM * FROM "log_err"(...);
            RETURN '';

    END
    $BODY$
      LANGUAGE plpgsql VOLATILE
      COST 100;
    ALTER FUNCTION get_columndef(regclass)
      OWNER TO postgres;

  
2014-09-12  
  
------

Socket 超时设置
=================
  
概要
----

代码中如何控制Socket超时，包括connect超时,recv超时,send超时。
  
说明
----
  
win平台和unix平台的socket函数并未提供明确的超时参数。  
查到的通常用于设置超时的方法有两种：  

* 利用setsockopt函数设置SO_SNDTIMO(send超时和connect超时)，SO_RCVTIMEO(recv超时)  
* 利用select间接实现超时设置  
  
方法1：setsockopt
..................
  
此函数用来设置socket的各种状态，这里主要是对SO_SNDTIMO与SO_RCVTIMEO这两个参数进行设置。  

send,recv超时：  
::

  windows:  
  int Timeout = 1000; // (ms)  
  setsockopt(socket, SOL_SOCKET, SO_SNDTIMEO, (char*)&Timeout, sizeof(int));  
  setsockopt(socket, SOL_SOCKET, SO_RCVTIMEO, (char*)&Timeout, sizeof(int)); 
  
  unix:  
  struct timeval Timeout = {1,0};  
  setsockopt(socket, SOL_SOCKET, SO_SNDTIMEO, (char *)&Timeout,sizeof(struct timeval));  
  setsockopt(socket, SOL_SOCKET, SO_RCVTIMEO, (char *)&Timeout,sizeof(struct timeval));  
  
connect超时：
::

  linux下connect超时时间与send超时时间相同，故可借用对SO_SNDTIMEO的设置来实现connect超时设定。  
  windows下暂未查到利用setsockopt进行connect超时设定的方法，但可利用下文的select来实现。  
  
方法2：select
..................
  
简单说select函数是对标识符(windows下称句柄)是否准备就绪的一个判断函数。  
函数阻塞等待，直到出现准备就绪的标识符(句柄)或超时。  
  
select在windows与unix下的实现不同，但作用相同。  
将select函数的标识符参数指定为socket，即可监视socket的状态。  
  
使用方法：  

默认状态下connect,recv,send处于同步状态，阻塞等待结果，如此不能发挥select的作用。  
需先将socket设为异步非阻塞，执行完connect,recv,send后由select等待结果，  
然后再根据需求将socket设回同步阻塞。  

以下代码以connect为例：  

.. code-block:: C

    fd_set  mFds;
    struct  timeval     mtimeout;

    // 超时时间设置
    mtimeout.tv_sec = 3;
    mtimeout.tv_usec = 0;

    // socket异步设定
    smfd = fcntl( mClient, F_GETFL, 0 );
    fcntl( mClient, F_SETFL, smfd | O_NONBLOCK );

    // connect
    mrc = connect( mClient, (struct sockaddr*)&mAddr, sizeof(mAddr) );
    if ( errno != EINPROGRESS ) {
        close( mClient );
        // error 
    }

    // connect timeout
    // select监测项目清空
    FD_ZERO( &mFds );
    // select监测项目设置
    FD_SET( mClient, &mFds );
    // select
    mrc = select(mClient + 1, NULL, &mFds, NULL, &mTimeout);
    if( FD_ISSET( mClient, &mFds ) == 0 ){
        mrc = -1;
    }

    // socket同步设定
    smfd = fcntl( mClient, F_GETFL, 0 );
    fcntl( mClient, F_SETFL, 0 );

注：recv与send的代码与connect相近，自己做的项目中采用select对connect  
和recv的超时进行了设置，理论上send也是可行的，但没有实际操作，使用前请确认。  


2014-07-29  
  
------

JS与C#相互调用
=================

背景
----

C#WinForm中使用WebBrowser访问网页，并与页面中JS通信。

实现
----

* 为使JS能访问C#中函数，需在C#代码中开启权限，并利用 **window.external** 进行调用
  **[System.Runtime.InteropServices.ComVisible(true)]**
* C#调用JS中函数时，要使用 **WebBrowser.Document.InvokeScript** 方法
  
示例代码：

(C# -> JS -> C#)

.. code-block:: JavaScript

    <script>
        function JSwebBrowserTest( a )
        {
            //alert(window.external);
            window.external.JSCall_Test();
        }
    </script>
  
.. code-block:: C#

    [System.Runtime.InteropServices.ComVisible(true)]
    public partial class Form1 : Form
    {
        public Form1
        {
            webBrowser.Document.InvokeScript("JSwebBrowserTest");
        }
        public void JSCall_Test()
        {
            MessageBox.Show("Hello Hanbin!");
        }
    }

  
注意
----

JS调用C#中函数并执行的时候，权限为调用方，非定义方。故被调用函数中若有涉及权限的处理，
可能会失败。  

项目现实中的情况是C#中定义了打印函数(C#利用打印机提供的SDK实现打印)，直接调用可以成功，
但JS中调用却失败(打印机SDK返回内部错误)。
解决方法，首先尝试委托和Invoke配合的方式，结果失败，这里需要注意的是，委托仍然是
以调用方权限来执行，而非委托定义方。
而后采用在新线程中执行打印函数，成功(JS->C#->create thread->printfunc)。
  
最初想到的是JS发送事件或者信号，C#端接受后，以自身权限来执行，但并未查找到相关方法。  
而新建线程的方式总让人怀疑是否是因为线程间调用使得打印机SDK产生错误。  
但打印机错误信息较少，内部又无法看到，暂且到此。  
  
2014-07-22
