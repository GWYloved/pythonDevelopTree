import requests

url = 'http://news.163.com/rank/'
response = requests.get(url)
content = response.content

print content.decode('gbk').encode('utf-8')