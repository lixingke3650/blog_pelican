rPSF-基于SFTP协议的文件传送工具
#######################################

:title: OrPSF-基于SFTP协议的文件传送工具
:date: 2014-06-23 13:00
:category: 项目
:tags: OrPSF, SFTP
:author: Hanbin

**源码托管地址： https://github.com/lixingke3650/OrPSF**

OrPSF -- 使用SFTP协议实现文件传送的小工具.  


起因
====

偶尔需要从linux上下载上传文件，但又不想安装winSCP等软件。
也不想在linux上开启ftp等服务。

SFTP
====

Secure File Transfer Protocol(SFTP)可以为文件传送提供一种
安全的加密方法。

SFTP是SSH的一部分，使用22端口，不需要额外开启服务或进程。

本程序借用 **psftp** 来实现sftp协议。

参考： http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html


OrPSF
=====

为提高兼容性，使用MFC编写，在 **psftp.exe** 基础上增加UI，便于使用。

熟悉命令行的朋友可直接使用psftp.exe.

* 使用管道对psftp.exe进行标准输入输出重定向。
* GUI方式 登录、上传、下载。
* 无需安装，解压即可使用。
* linux端只需开启SSH。

后续
====

目前利用psftp来实现SFTP的认证与通信。
后续考虑自己编码实现该功能。


以上。
20140623
