#coding:utf-8
import requests
import json
# requests 如何测试各种http接口
#1. 无参的get
#
# res = requests.get(url='http://www.baidu.com')
#
# #2 有参数的get
# res = requests.get(url='', params={'a': 'b'})
#
# #3 有正文体的post请求
# # 1.url-encode
# res = requests.post(url='', data={}, headers={'content-type': 'application/x-www-form-urlencoded'})
#
# #2. raw  xml  -- json
# #xml
# xml = ''''''
# res = requests.post(url='', data=xml, headers={'content-type': 'text/xml'})
#
# #json
# data = {'y': '123'}
# res = requests.post(url='', data=json.dumps(data, ensure_ascii=False), headers={'content-type': 'application/json'})
#
# res = requests.post(url='', json=data,  headers={'content-type': 'application/json'})

# 3 form表单
# 无需配置头信息
# res = requests.post(url='http://139.199.132.220:9000/event/index/submit_info/',
#               data={'username': 'wwq1', 'password': '123456', 'email': 'qqq@163.com'})
#
# print res.text

# file-form
#二进制流格式   open
# res = requests.post(url='http://139.199.132.220:9000/event/index/uploadFile/',
#               files={'myfile': open('D://demo.html', 'rb')})
# print res.text


#下载接口
# res = requests.get(url='http://139.199.132.220:9000/event/index/export/')
#
# with open('./user.csv', 'wb') as f:
#     for i in res.iter_content(128):
#         f.write(i)


#请求响应时间

# res = requests.get(url='http://www.baidu.com')
# print int(round(res.elapsed.total_seconds()*1000))

# cookies = {'token': '11111111', 'uid': '1'}
# requests.post(url='', headers='', cookies=cookies)

# 获取响应的值



# python 解析xml
# from xml.etree import ElementTree as ET
#
# res = requests.get(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString?theRegionCode=3113')
# # print res.text
# # ET.parse('./1.xml')
#
# print len(ET.fromstring(res.text).findall('.//{http://WebXml.com.cn/}string'))

# python 解析json
import json
res = requests.post(url='http://139.199.132.220:9000/event/weather/getWeather/', json={"theCityCode": 1},
              headers={'content-type': 'application/json'})

print res.text
# print json.loads(res.text)['date']
data = {
    "event_list": [
        {
        "id": "1",
        "title": "红米新品发布会",
        "status": 1,
        },
        {
        "id": "32",
        "title": "锤子秋季新品发布会",
        "status": 2,
        }
    ],
    "error_code": 0
}
import jsonpath

print jsonpath.jsonpath('', '$.event_list.id')
