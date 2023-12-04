CentOS下搭建Apache+PHP+FMS环境
######################################

:title: CentOS下搭建Apache+PHP+FMS环境
:date: 2014-05-16 15:30
:category: 整理
:tags: Linux, FMS, CentOS, Apache, PHP
:author: Hanbin

------

网上有很多相关的介绍，这里只记录下流程和我安装过程中遇到的问题。
接到的要求是在 **CentOS6.4** 下安装 **FMS3.5** 和 **PHP5.4.20** 。

FMS安装
=======

FMS(Flash Media Server),简单来说提供了网络视频服务的中间件。
支持RTMP协议。
FMS的安装并不困难，解压后执行下面语句即可。
::

  \# ./installFMS

安装时请注意端口(RTMP端口，默认1935和80；管理端口，默认1111)配置，
最后会询问是否安装Apache，这里将额外安装Apache，故此处选择否。

安装完成后发现FMS启动失败，经排查，FMS服务共需4个线程:
::

  * fmsmaster
  * fmsadmin
  * fmscore
  * fmsedge

其中fmsedge线程启动的连接库文件(**libcap.so.1**)缺失导致 **启动失败** 。

新版Linux将原本位于/usr/lib下的libcap.so.1移动到了/lib下，并改名为/lib/libcap.so.2.16。
做如下连接，可解决问题。
::

  \# ln -s /lib/libcap.so.2.16 /usr/lib/libcap.so.1

(此处若安装FMS自带的Apache服务，还需要做 **libexpat.so.0** 文件的连接:
ln -s /lib/libexpat.so.1.5.2 /usr/lib/libexpat.so.0)


FMS配置
=======

默认状态下，FMS被安装到/opt/adobe/fms路径下，打开/opt/adobe/fms/conf/fms.ini文件，作如下设置:

::

  * ADAPTOR.HOSTPORT = :1935      (rtmp用端口)
  * HTTPPROXY.HOST = :8134        (与Apache Listen端口相同)

设置完成后，重启FMS服务:

::

  \# /opt/adobe/fms/fmsmgr server fms start      -- 开启 FMS Service
  \# /opt/adobe/fms/fmsmgr server fms stop       -- 停止 FMS Service
  \# /opt/adobe/fms/fmsmgr server fms restart    -- 重启 FMS Service


Apache安装
==========

图方便，利用yum工具安装Apache，名字有些霸道 - **httpd** ,为了实现PHP安装需要安装 **http-devel**

::

  \# yum -y install httpd-devel


Apache配置
==========

安装完成后打开配置文件，设置使之可用于PHP。

::

  \# vi /etc/httpd/conf/httpd.conf

1 修改web文件路径

::

    DocumentRoot "../webroot"  
     ↓  
    DocumentRoot "opt/adobe/fms/webroot"  

2 在#AddType application/x-tar .tgz下面追加如下内容:

::

  AddType application/x-httpd-php .php
  AddType application/x-httpd-php-source .phps 

如需要自启动，执行如下语句:

::

  \# chkconfig httpd on


PHP安装
=======

这里采用编译安装的方式，首先下载源码，**wget** 之。
解压并进入目录后，执行如下命令安装:(PHP安装需要libxml2的支持，请提前确认) 

::

  \# ./configure --prefix=/usr/local/php --with-apxs2  
  \# make  
  \# make install

PHP配置
=======

执行如下命令，创建PHP配置文件:
(此处假定PHP安装文件解压目录为/tmp/php-5.4.20,PHP安装路径为/usr/local/php)
::

  \# cp /tmp/php-5.4.20/php.ini-development /usr/local/php/lib/php.ini


动作测试
========

配置完成后，重启Apache，分别测试FMS与PHP是否安装成功。

1 测试FMS可直接在浏览器中输入 **[ipaddr]:8134**  
若页面打开并在RTMP方式下有动画出现，则FMS安装成功。

2 测试PHP，可用个测试文件测试一下是否成功。

.. code-block:: PHP

    <?php 
    phpinfo(); 
    ?>

保存为phpinfo.php,放入/opt/adobe/fms/webroot下  
浏览器中输入 [ipaddr]:8134/phpconf.php  
若正常打开并显示服务器PHP信息，则安装成功！  


总结
====

| 由于FMS版本较老的原因，一些链接库已经不存在或移动了，导致FMS启动失败
| 按上述设置仍不能正常动作，请尝试关闭系统 **SELinux** 与 **iptables**

SELinux与iptables关闭后，不能保证系统安全，相关配置请参考本博客--Linux服务器安全设置  


| 以上  
| 2014.05.16
