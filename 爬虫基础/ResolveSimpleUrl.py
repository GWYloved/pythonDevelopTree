#encoding:UTF-8
import urllib
import urllib.request

# 用这个做百度查询


data = {}
data['word'] = 'hehe'

url_value = urllib.parse.urlencode(data)
url = 'http://www.baidu.com/s?'
full_url = url+url_value

data = urllib.request.urlopen(full_url).read()
data = data.decode("UTF-8")
print(data)