import urllib.request
import urllib.parse
import json

content = input("请输入需要翻译的内容：")
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com"
head = {}
head['Referer'] = 'http://fanyi.youdao.com/'
head['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data, headers=head)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
target = json.loads(html)
print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
print(req.headers)
