Linux下程序守护-OrMonitor
#############################

:title: Linux下程序守护-OrMonitor
:date: 2014-10-15 21:00
:category: 项目
:tags: Linux, OrMonitor, start-stop-daemon
:author: Hanbin

------

起因
====

之前学习Gunicorn时突然想到，如果Gunicorn运行过程中出现错误，自行退出，
而管理员又不能及时发现，这就严重影响体验了。还好Gunicorn官网推荐了
管理工具，比如Gaffer和Supervisor。

不仅是gunicorn，工作中也遇到过项目进程出错退出的情况，所以还是自己尝试
写一个工具，方便灵活还可以顺便学习。

-------

OrMonitor
==========

这个工具可用来监视指定程序是否运行中，若程序未运行，则重启程序。

前提
====

> 利用**start-stop-daemon**命令来重启程序，故系统要安装上start-stop-daemon工具
> 监控对象需要生成pid文件，若不能生成，推荐使用start-stop-daemon来启动程序
> (使用**-pidfile**和**-m**参数，自动生成pid文件)或者由OrMonitor来启动程序

程序存在否判断方法
=====================

> 首先判断监控对象的pid文件是否存在，不存在则认为程序未启动
> 若pid文件存在则读取内容，判断读取到的pid号的进程是否存在,不存在则认为程序未启动
> 上述作业定期启动，若发现进程未运行，则启动程序

注：监控对象需要生成pid文件，若不能自行生成则由start-stop-daemon代为生成
  
运行流程
=========

> 1.读取配置文件并计算监控周期(去各监控对象周期的最小公约数)
> 2.启动定时器，定时信号到达时判断各对象是否到达监控周期
> 3.到达监控周期则判断程序是否存在
> 4.进程不存在则按照读取的配置来启动进程

配置文件
========

配置文件样例如下：

.. code-block:: Ini

    [nginx]
    #name = nginx
    bin = /usr/local/nginx/sbin/nginx
    parame = 
    pidfile = /usr/local/nginx/logs/nginx.pid
    cycle = 60000

    [gunicorn]
    #name = gunicorn
    bin = /usr/local/bin/gunicorn
    parame = -c /usr/local/nginx/App/video/gunicorn.conf.py index:app
    pidfile = /var/run/gunicorn.pid
    cycle = 10000

各项目解释：
::

    [nginx]-名称
    bin-程序可执行文件路径
    parame-运行参数
    pidfile-程序运行时生成的pid文件
    (注意，若程序自行生成pid文件，则要确保此处指定的路径与程序自行生成pid文件的路径相同。
    若程序不生成pid文件，推荐用start-stop-daemon启动程序并追加**-pidfile**和**-m**参数来
    生成pid文件。或者直接由OrMonitor来启动程序。)
    cycle-检测周期


源码
====

请参见：
  https://github.com/lixingke3650/OrMonitor

待追加功能
==========

* 以守护进程形式启动OrMonitor
* 服务配置(init.d)


20141015

以上。
要成功了吗