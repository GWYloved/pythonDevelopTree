#coding:utf-8
import urllib,urllib2

url = 'http://www.baidu.com/s'
data = {
	"wd":"宁哥的小站"
}
data = urllib.urlencode(data)
ful_url = url+'?'+data
print ful_url
response = urllib2.urlopen(ful_url)
print response