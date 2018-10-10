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

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action'
headers = {'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
formdata={
    'start':'0',
    'limit':'10'
}
data = parse.urlencode(formdata).encode('utf-8')
req = request.Request(url,data=data,headers=headers)
response = request.urlopen(req)
html = response.read().decode()
print(html)
results = json.loads(html)

for item in results:
    print(item['title'])


