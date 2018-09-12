#coding:utf-8
import requests
import base64
import json
import util

# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# data = {'username':'huice', 'password': base64.encodestring('123huicehuice!@#')}
# res = requests.post(url='http://139.199.132.220:9000/event/api/register/',
#               headers=headers,
#               data=data)
# print res.status_code
# print json.loads(res.text).get('token')

url = 'http://139.199.132.220:9000/event/api/add_event/'
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': 'token=75ff30521dd7bafb48e07cf7e0a0b564dd8896a4;uid=1'}
data = {
    'title': '慧测接口测试',
    'time': '2018-09-01 15:00:00',
    'address': '汤立路220号1号楼007',
}
sign = util.create_sign('75ff30521dd7bafb48e07cf7e0a0b564dd8896a4', data)
data['sign'] = sign
res = requests.post(url=url,
              headers=headers,
              data=data)
print res.status_code
print res.text


