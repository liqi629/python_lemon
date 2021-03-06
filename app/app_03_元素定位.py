#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
app_第2周—第1課_1
一、关于启动参数，其他可能用到的启动参数（不太常用的暂时不讲）
必须：
automationName
platformName
platformVersion
deviceName
appPackage
appActivity

重要：
caps["noReset"]=True  ---很重要，基本都会写，针对应用，不重置/重置
unicodeKeyboard --- 如果要输入中文，可以打开Unicode输入法，默认关闭
resetKeyboard --- 测试结束后重置输入法到原有状态，与unicodeKeyboard结合使用

之后做小程序会用：
browserName --- 浏览器名称
chromedriverExecutable --- chromedriver执行路径
chromeOptions

不太用：
app --- 会重新安装，如果已经安装了，就不要使用这个命令。很少用
fullReset --- session结束后会卸载，可以与app配合使用。一般不用
adbPort --- 默认5037，如果不是则自己重新指定

二、appium自动化与selenium操作库的关系
1.查看源码，很多都是从selenium导入或继承的，然后再新增app自己的方法。
from appium import webdriver
2.我们只需要学习app不同的方法即可

三、元素定位
方式1：通过Android SDK自带的定位工具uiautomatorviewer查看
我这里的路径（通过环境变量查看android_home）：C:\Users\lipan\AppData\Local\Android\Sdk\tools\bin
双击uiautomatorviewer.bat进入查看界面；
然后点击 device screenshot按钮，即可进入元素查看页面
前提：设备已经连接；且未被其他占用如appium，同时只能被一个程序使用；并且打开app页面
补充：怎么看坐标？左上角最小，横轴向右增大、纵轴向下增大。
class---代表元素类别，如android.widget.TextView，类似于tag_name标签名，大部分情况不唯一 （这个定位不能用tag_name要用class_name）
resource_id---如com.dangdang.reader:id/nickname_tv，是app中最常用的定位方式，大部分都是唯一的；
如果不唯一（比如布局完全一样的几个元素），可以通过find_elements找到后用下标区分
text---文本信息，如“点击登录/注册”
content_desc ---描述文案

八大元素定位中，只有3种可以用于app：id（即resource-id）、class_name(即class)、xpath
其他5种不支持app：name、tag_name、link、partial_link、css
另外还有2种app独有常用的：
driver.find_element_by_accessibility_id() ---即content_desc
driver.find_element_by_android_uiautomator()  ---之后单独再讲
以上5种是app最常用的定位方式。
其中id是最常用的，class_name很少用，xpath是官方不推荐使用的，因为定位较慢，实在没有其他方式可以定位，也是可以用的。
（xpath在web中使用的非常多，但是在app不是很常用）
（文本也可以，之后再补充）

提问：app的xpath定位怎么写？---跟web套路一样
//android.widget.TextView[@resource-id='com.dangdang.reader:id/tv_task']   ---以福利入口为例
//*[@text='福利']   ---text在app中当做属性使用，是@text；与web中text()不同。


===app_第2周—第1課-1小时10分钟===
PPT总结：
appium-app页面元素定位
1.通过id定位元素：resource-id
2.通过ClassName定位：classname
3.通过AccessibilityId定位：content-desc
4.通过AndroidUiAutomator定位
5.通过xpath定位
6.坐标
# 常用元素定位
# driver.find_element_by_id()
# driver.find_element_by_class_name()
# driver.find_element_by_accessibility_id()
# driver.find_element_by_android_uiautomator()
# driver.find_element_by_xpath()

===关于AndroidUiAutomator定位===
独立于appium和selenium框架，是安卓自带的框架，使用java语言写的。
主要关注UISelector类，只有这个类与元素定位有关。
注意查看官方文档，需要翻墙，学习包里面有。
先实例化再调用其方法UiSelector()
我们常用的定位方法这里都有，
比如id这里有resourceId(String id)和resourceIdMatches(String regex)正则匹配
比如text这里有text(String text)全匹配，以及textContains(String text)部分匹配等4种。
比如content-desc这里有description(String desc)全匹配，以及descriptionContains(String desc)部分匹配等4种。
比如classname这里有className(String className)等3种。
用法：
driver.find_element_by_android_uiautomator()
以文本举例。因为文本只支持uiautomator和xpath，但是在APP中xpath不是最推荐的。所有我们这里用uiautomator来写。
# uiautomator用法
# locator_fuli = 'new UiSelector().text("福利")'     # 注意：单引号里面是java代码，在java中字符串必须使用双引号
# locator_fuli = 'new UiSelector().text("福利").resourceId("resource-id")'  # 方法返回的的都是UiSelector，可以直接组合定位
# driver.find_element_by_android_uiautomator(locator_fuli)

补充：如果确定我们的定位是唯一的？可以尝试以下方法
(1)更新uiautomator之后，能在元素定位看到增加3行数据：xpath相对定位、xpath绝对定位、UiSelector定位
从xpath可以看到,如果resouce-id是唯一的，这里就只会显示xpath相对定位//class[@resouce-id=""]
(2)可以直接在appium的元素定位来查看定位信息
从find by查看，如果xpath是相对定位//class[@resouce-id=""]，说明resouce-id是唯一的。如果显示的xpath绝对定位，则不是唯一。
（3）还有一种查看元素定位的方式---python独立的元素定位框架
百度搜索python uiautomator2 github
https://github.com/openatx/uiautomator2

===app_第2周—第1課-end===
'''
