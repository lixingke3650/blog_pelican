Felica NFC开发
#################

:title: Felica NFC开发
:date: 2014-06-11 19:00
:category: 整理
:tags: Felica, NFC
:author: Hanbin

Felica NFC开发
===============

先介绍两个免费的SDK：

* 桌面环境: http://felicalib.tmurakam.org/
* Android: http://d.hatena.ne.jp/Kazzz/

下面是以前做项目时写在CSDN上的，转到这里来。

--------

1 NFC支持否的判断  
  
  NfcAdapter.getDefaultAdapter() - 获取当前系统下NFC适配器对象  
  
  getPackageManager().hasSystemFeature(PackageManager.FEATURE_NFC) - 获取应用是否支持NFC  
  
2 NFC是否有效判断  
  
NfcAdapter.getDefaultAdapter()isEnabled() - 当前NFC适配器是否处于有效状态  
  
3 NFC检测通知  
  
  两种方式:  
  
    1)  系统检测到NFC卡后，根据注册的应用信息，选出可处理NFC卡的应用并启动，若多于一个，则弹出列表供用户选择  
  
    2)  利用 adapter.enableForegroundDispatch() 来指定检测通知对象，函数参数包括应用的Activity或广播,检测的卡类型等，系统检测到卡后直接向该应用发送Intent,应用中onNewIntent被启动（也可发送广播，自定义BroadcastReceiver来接受该广播）  
