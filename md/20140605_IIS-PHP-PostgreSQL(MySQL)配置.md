Title: IIS-PHP-PostgreSQL(MySQL)配置
Date: 2014-06-05 21:00
Category: 整理
Tags: IIS, PHP, PostgreSQL, MySQL
<!-- Slug:  -->
Author: Hanbin
<!-- Summary: 第一篇日志 -->


IIS-PHP-PostgreSQL(MySQL)配置
=============================
  
  
IIS安装
----
IIS是微软推出了Web服务器，同Apache，Nginx差不多，市场份额处在上升中，  
windows已经自带了IIS功能，但并未开启，需要到控制面板中添加。  
因为是图形化界面，相关配置也比较容易。安装完成后，为了配合PHP，  
需要在**IIS管理**-**映射控制**中添加PHP的模块映射。  
  
* 路径： *.php  
* 模块： FastCgiModule  
* 执行文件： D:\Program Files\PHP\PHP_ts\php-cgi.exe **-根据PHP安装路径来配置**  

配置完成后新建Web站点，即可。  
  
  
PHP安装
----
Windows下的PHP是一个绿色包，解压即可。  
下载的时候有两个选择:   

* PHP_ts  
* PHP_nts  
  
简单查了一下，好像是线程安全方面有些差异。  
  
  
PHP配置
----
打开PHP安装目录下的**php.ini**文件。修改如下地方：  
  
* extension_dir = "D:\Program Files\PHP\PHP_ts\ext"  - 指向安装目录下ext文件夹  
* extension=php_mysql.dll        - MySQL支持  
* extension=php_mysqli.dll
* extension=php_pdo_mysql.dll
* extension=php_pdo_pgsql.dll    - PostgreSQL支持  
* extension=php_pgsql.dll
* date.timezone = Asia/Tokyo     - 加入所在地时区信息  
  

PostgreSQL安装
----
从官网上下载安装包安装即可，安装过程中需要指定软件安装路径及数据库存放路径，没有特别需要注意的地方。  
默认登录用户： **postgres**, 连接端口： **5432**。  
  

PostgreSQL配置
----
主要配置文件有三个：  

* postersql.conf - 存放在数据库路径下  
* pg_hba.conf    - 同上  
* pgpass.conf    - 存放在C盘用户路径下  
  
PostgreSQL配合IIS+PHP并无特别需要修改的地方。  
  
  
PHP-PostgreSQL连接
----
  
代码如下，注意各个数据库连接方式有区别:  

`$dbsn = new PDO("pgsql:host=localhost port=5432 dbname=name user=user password=xxxx");`


:MySQL的配置
----
  
windows下**PHP+MySQL**的配合如果不能正常正常连接，  
可能还需要**libmysql.dll**，**php5ts.dll**的支持。  
