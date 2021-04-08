import urllib.request
import urllib.parse #主要用来把URL字符串拆分成URL组件，或者把URL组件拼装成URL字符串
import json

content = input("请输入需要翻译的内容：")
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com"
data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')  # 转换格式并编码为utf-8
response = urllib.request.urlopen(url, data)  # post请求必须带上data参数
html = response.read().decode('utf-8')
target = json.loads(html)
print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))  # 一层一层剥掉
