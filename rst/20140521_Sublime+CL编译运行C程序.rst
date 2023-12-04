Sublime + CL 编译运行C程序
##################################

:title: Sublime + CL 编译运行C程序
:date: 2014-05-21 13:50
:category: 整理
:tags: Sublime, CL.exe
:author: Hanbin

Sublime + CL 编译运行C程序
==========================

**Sublime** 是个文本编辑器，对于程序员来说又是一个轻量级IDE。

**CL.exe** 是微软的编译器，类似于GCC。

本文介绍是如何在Windows下，利用Sublime和CL来实现编译运行。

-------

Sublime没有自带编译器，为了实现编译运行，需要指定外部编译器。

目前常用的C/C++编译器有GNU的GCC(G++)和微软的CL。

查看文件 ** Sublime Text 2\Data\Packages\C++\C++.sublime-build ** 发现,Sublime通过
调用系统CL命令来启动编译器，但CL安装后相关的库文件与链接库没有添加到环境变量中。
(借助安装Visual Studio可完成CL的安装。是否可以单独安装命令行版的CL，没有调查)

添加的环境变量有如下几项(以VS2008为例，可参考Microsoft Visual Studio 9.0\Common7\Tools\vsvars32.bat脚本)

**PATH** 中添加:

* C:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE  
* C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN  
* C:\Program Files\Microsoft Visual Studio 9.0\Common7\Tools  

**LIB** 中添加:

* C:\Program Files\Microsoft SDKs\Windows\v6.0A\Lib  

**INCLUDE** 中添加：  

* C:\Program Files\Microsoft SDKs\Windows\v6.0A\Include  

保存后重启Sublime，** Ctrl + B ** - 编译,  ** Ctrl + Shift + B ** - 编译运行。
