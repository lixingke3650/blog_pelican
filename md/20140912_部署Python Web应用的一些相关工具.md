Title: 部署Python Web应用的一些相关工具
Date: 2014-09-12 20:00
Category: 整理
Tags: Python, Web
<!-- Slug:  -->
Author: Hanbin
<!-- Summary: 第一篇日志 -->

  
整理一些部署Python网络应用时可能用到的工具。  
  
----
## OS  
  
作为网络服务器的运行平台，主要有Windows和Unix两种，  
两个平台下都有对应的解决方案，但目前来看，Unix(Linux)下  
的工具要更丰富些。  

## Apache、Nginx、IIS
  
这些都是网络服务器，用来接受并分发来自网络的请求。  
Apache： 目前占有量最大的服务器，但并发量一直为人诟病。可能与其  
采用的select模型有关。  
Nginx： 占有率呈上升状态，抗压性非常优秀。  
以上两个都支持Windows和Unix平台,但由于两平台上的底层网络实现形式不同，  
故大部分评测都是基于Unix版本进行的。  
IIS: 只支持Windows平台，自身带有asp解析器等，  
在windows平台上推荐采用此服务器。  
  
## Tomcat、Openasp  
  
这些可能跟主题部署Python应用没啥关系，不过为了完整性也一起说一下。  
Tomcat主要用来解析jsp，Openasp是一种asp的解析器，使得IIS以外的网络服务器也可以  
支持asp的网页。不过目前来看无论jsp还是asp，市场占有都不理想。  
暂且将他们归为解析器吧，与之相对的还有PHP解析器，Ruby解析器，Python解析器等。  
但后者除网络外显然还能完成更多工作。(PHP目前主要被用于Web)  
脱线了。。。  
  
## CGI、FastCGI、SCGI、WSGI、uWSGI  
  
这些是通用网关接口的各个不同实现协议。  
CGI，把它定义为一种协议还是一个实现呢，有些纠结。  
比较古老了，工作方式也很直接，来一个请求新建一个线程去执行。  
FastCGI对CGI进行了改进，最大的不同是FastCGI同时启动多个线程，  
有新请求时，用空闲线程去执行，节省了线程启动与内存分配所花费的时间。  
SCGI，CGI的一种简化，没有详细的调查，好像应用不是很多。  
WSGI，Python专属的一种接口协议，不过由于优秀的性能也被其他平台所借鉴。  
uWSGI是接口协议也是一种实现，下文中介绍。  
  
## flup、spawn-fcgi、Gunicorn、uwsgi  

这些都是协议的具体实现，是我们可以利用的实实在在的工具。  
flup: Python的通用网关接口实现，支持FastCGI，SCGI协议。  
spawn-fcgi： FastCGI的一个管理软件，支持FastCGI协议。  
Gunicorn： 解析WSGI协议的服务器，用在这里可以理解为通用网关接口的实现。  
uwsgi： 如前文所说，它即是通用网关协议，又是该协议的一种实现。  
  
目前应用中FastCGI应该比较普遍，但Gunicron是一种发展趋势，毕竟WSGI  
被认定为Python的标准网关接口。  
而uwsgi采用自己的协议，以后发展如何不好评价。
有评测说性能上 uwsgi > Gunicorn > FastCGI,   
也有人发文说uwsgi的稳定性不如Gunicorn。  
这些都是从别处看到的结论，未必真实。  
  
## Django、Tornado、web.py、Flask、Pylons、Bottle等  
  
这些都是Python的网络框架，可帮助我们快速的开始网页编写，  
并提供了一些辅助工具等。  
  
----

利用以上这些工具完全可以部署一个自己的Python应用。  
以下的内容可能与Python的网络应用没啥大关系。  

## Greenlet、Stackless python  
  
Greenlet、Stackless python是完全不同的两个东西，  
将他们放到一起是因为都是Python的异步解决方案。当然异步处理  
还包括Python自带的Threading，Thread模块。  
  
Stackless python是对Python的重写，极大提高了Python的并行处理能力。  
有测评说与Python标准的thread不在同一数量级上。  
Greenlet是在同一个线程内，对程序进行优化处理，有效减少了IO等待等，  
以此提高程序的运行效率。它有一个时髦的名字：协程。  
  
## Concurrence、Eventlet、Gevent  
  
这些都是对 Greenlet 的实现，好像Gevent在国内用的人比较多，  
有对比说Gevent比Eventlet的性能也要好些，没有自己测试，仅作参考吧。  
之所以提到异步处理，是因为前文中的Gunicorn可借助Gevent等提升性能。  
  
----
差不多了，还有需要的话后续补充！  
另外，这些都是自己的理解，请酌情参考。  
20140912  
  
以上。  
