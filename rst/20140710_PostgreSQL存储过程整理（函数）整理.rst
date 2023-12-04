PostgreSQL存储过程(函数)整理
#############################

:title: PostgreSQL存储过程(函数)整理
:date: 2014-07-10 22:00
:category: 整理
:tags: 数据库, PostgreSQL
:author: Hanbin

------

传说大阪将在今明两天迎来台风，一旦政府发布暴风警报，公司员工将全体放假。
这等喜讯传来，我等草民怎能不欢心雀跃加不已。
一大早黑云密布，确是灾难来临的前兆，计划着电视剧游戏加睡觉的不知不觉中，
外面的天空竟愈发晴朗起来，一同晴朗的还有项目组长那张猥琐的脸，
这台风也太他妈不给力了吧。
  
------

最近项目用到PostgreSQL的存储过程，之前没接触过，记录一下常用的函数，方法等。  

内部函数：  

* 字符串拼接：　CONCAT  
* 字符串截取： substring  
* 字符串分割并返回指定位置值: split_part(string text, delimiter text, field int)  
* 转换为字符串：　to_char　(区别于Oracle,好像不支持进制转换)  
* 转换为数字：　to_number  
* 获取当前时间(TIMESTAMP)：　now()  
* 字符串转换为时间(TIMESTAMP)：　to_timestamp()  
* 时间(TIMESTAMP)截取:　date_trunc()  
* 类型转换：　CAST()  
* 四舍五入：　round()  
* 随机数：　　random() (0~1之间，若要求取A~B之间的随机数，可利用(round(random()*(B-1))+A))  


待补充。  
