import urllib, urllib2
url = "http://www.douban.com/"
data = {
	"form_email":"15000897584"
	"form_password":"dream.2012"
}
data = urllib.urlencode(data)

request = urllib2.Request(url=url,data=data)
response = urllib2.urlopen(request)
print response.read()