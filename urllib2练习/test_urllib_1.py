# coding:utf8
import urllib2
import cookielib

url = 'http://www.baidu.com'

# urllib2使用方法一：直接解析网页，getcode（）为200代表成功，返回网页长度
print'no.1'
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

# urllib2使用方法二：添加request的内容，模拟一个浏览器（类似于data），解析request
print 'no.2'
request = urllib2.Request(url)
request.add_header('user-agent','Mozilla/5.0')
response2 = urllib2.urlopen(request)
print response1.getcode()
print len(response2.read())

# urllib2使用方法三：增加一个cookielib的cookiejar，使用httpcookieprocessor进行解析此cookiejar
# 同时构造一个opener，使用install_opener安装这个opener
# 之后的url的打开，就带有了此opener的环境
print 'no.3'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print len(response3.read())