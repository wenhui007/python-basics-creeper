"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from urllib import request
from urllib import parse
import json

#Request_URL='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
Request_URL='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# formdata 的字典
Form_Data = {}
Form_Data['i'] = 'Tom'
Form_Data['from'] = 'AUTO'
Form_Data['to'] = 'AUTO'
Form_Data['smartresult'] = 'dict'
Form_Data['client'] = 'fanyideskweb'
Form_Data['salt'] = '1537857955340'
Form_Data['sign'] = '6b7991fb756c4184630db11382d640b0'
Form_Data['doctype'] = 'json'
Form_Data['version'] = '2.1'
Form_Data['keyfrom'] = 'fanyi.web'
Form_Data['action'] = 'FY_BY_REALTIME'
Form_Data['typoResult'] = 'false'

data = parse.urlencode(Form_Data).encode('utf-8')
headers = {'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
req = request.Request(Request_URL,headers=headers)
# post请求
response = request.urlopen(req,data=data)
# 读取请求的结果
html = response.read().decode()
print(html)
translate_result = json.loads(html)
result = translate_result["translateResult"][0][0]['tgt']
# 打印翻译结果
print('翻译的结果：',result)




