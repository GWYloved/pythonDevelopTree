import urllib2
url = 'http://www.baidu.com'
response = urllib2.urlopen(url)
content = response.read()
print response.headers
print content