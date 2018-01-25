import urllib2
url = 'http://www.baidu.com'
response = urllib2.urlopen(url)
content = response.read()
content = content.decode("UTF-8")
print response.headers
print content