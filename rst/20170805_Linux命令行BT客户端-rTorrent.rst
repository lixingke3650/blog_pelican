Linux命令行BT客户端-rTorrent
####################################

:title: Linux命令行BT客户端-rTorrent
:date: 2017-08-05 15:00
:category: 整理
:tags: rTorrent
:author: Hanbin


电脑重装了Debian9，Wifi总需要登陆到桌面后才能自动连上。

不知道是不是换到Xfce的原因。总之，Wifi要比有线来的麻烦。

安装与使用
-----------

老电脑了，闲着也是闲着，不如让它充当个下载工具。
将我的SSD从迅雷中解放出来，说不好还能增加点寿命。

rTorrent是Linux下命令行BT客户端。好像是从archlinux发起的。

不管，安装到我的Debian上。

* apt-get install rtorrent

(Debian9上已经默认不安装aptitude了，网上查了资料，国内的凡是提到apt-get与aptitude的，
基本上一边倒的支持aptitude. 国外的帖子却有说最近apt-get进展神速，在解决包依赖这个话题上上已经不输aptitude.
我也就随便看看，没有深入调查研究。再说我也不是什么重度用户，也体会不出两者的差别，安心的用apt-get吧。)

写完上面一大段，发现rTorrent已经被安装到我的Debian9中了。
先来下载个文件试试。找到个三国志10PK的种子，wget到本地目录。
下面分步骤来说明下载过程：

1. 键入rtorrent启动

2. 输入种子名称，回车载入种子

3. 按方向键选择已经载入的种子

4. 选好种子后按 **Ctrl+s** 来启动下载

5. 其他一些快捷键： **Ctrl+d** ： 停止下载； **Ctrl+q** ： 退出rtorrent


更好的工作
-----------

通过配置文件，可以让rtorrent更好的工作。

rtorrent启动后会自动载入位于用户根目录下的配置文件(~/.rtorrent.rc)，

并按照设定初始化。

::

    #下载目录 
    directory = ~/Downloads
    #下载历史目录（此目录中包括下载进度信息和DHT节点缓存）
    session = ~/Downloads/session
    #最小允许peer数
    min_peers = 1
    #最大允许peer数
    max_peers = 50
    #最大同时上传用户数
    max_uploads = 1
    #最大下载 k/s
    download_rate = 2000
    #最大上传 k/s
    upload_rate = 10


以上。

20170805

新疆
