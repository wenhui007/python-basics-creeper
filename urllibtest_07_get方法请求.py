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
import  chardet

url= 'https://www.baidu.com/s?'
word = {'wd':'中秋节'}
#对字典进行编码，转换成url编码格式的字符串
word = parse.urlencode(word)
print(word)
new_url = url + word
headers = {'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
req = request.Request(new_url,headers=headers)
response = request.urlopen(req)
html = response.read()
#print(html)
charset = chardet.detect(html)['encoding']
print(charset)
html = html.decode(charset)
print(html)