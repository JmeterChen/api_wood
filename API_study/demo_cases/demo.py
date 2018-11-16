# coding:utf-8
import requests
import jsonpath

# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")


# import json
# requests 如何测试各种http接口
# 1. 无参的get
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
# #2. raw文本格式  xml格式或者json格式   这里的xml和json都是字符串
# #xml
# xml = ''''''
# res = requests.post(url='', data=xml, headers={'content-type': 'text/xml'})
#
# #json
# import json
# data = {'y': '123'}
# res = requests.post(url='', data=json.dumps(data, ensure_ascii=False), headers={'content-type': 'application/json'})
#
# res = requests.post(url='', json=data,  headers={'content-type': 'application/json'})

# 3 form表单  # 无需配置头信息

# res = requests.post(url='http://139.199.132.220:9000/event/index/submit_info/',
#                     data={'username': 'wwq1', 'password': '123456', 'email': 'qqq@163.com'})
#
# print res.text

# # 4 file-form
# # 二进制流格式文件   open  若果上传的是文件  那么参数应该是files
# res = requests.post(url='http://139.199.132.220:9000/event/index/uploadFile/',
#                     files={'myfile': open('D://demo.html', 'rb')})
# print res.text


# 下载接口
# res = requests.get(url='http://139.199.132.220:9000/event/index/export/')

# print(res.text)  # 如果文件是文本格式，可以直接打开显示
# print(res.content)  # 若果文件是二进制文件 可以通过content显示出来

# # 将下载的文件写进指定的文件里
# with open('./user.csv', 'wb') as f:
#     for i in res.iter_content(128):
#         f.write(i)


# # 请求响应时间
#
# res = requests.get(url='http://www.baidu.com')
# print(res.elapsed.total_seconds()*1000)   # ms级别
# # print int(round(res.elapsed.total_seconds()*1000))
# #
# # cookies = {'token': '11111111', 'uid': '1'}
# # requests.post(url='', headers='', cookies=cookies)


# 获取响应的值
# python 解析xml
# 包1：xml.dom  包2：xml.etree
# from xml.etree import ElementTree as ET
# res = requests.get(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString?theRegionCode=3113')
# print res.text
# ET.parse('./1.xml')  # 从xml文件中解析xml

# print(ET.fromstring(res.text).findall('.//{http://WebXml.com.cn/}string')[1].text)
# print len(ET.fromstring(res.text).findall('.//{http://WebXml.com.cn/}string'))  # 从字符串中解析xml

# # # python 解析json
# import json
# res = requests.post(url='http://139.199.132.220:9000/event/weather/getWeather/',
#                     json={"theCityCode": 1},
#                     headers={'content-type': 'application/json'}
#                     )

# print res.text
# print json.loads(res.text)['date']
# print jsonpath.jsonpath(res.json(), '$.date')

# data = {
#     "event_list": [
#         {
#         "id": "1",
#         "title": "红米新品发布会",
#         "status": 1,
#         },
#         {
#         "id": "32",
#         "title": "锤子秋季新品发布会",
#         "status": 2,
#         }
#     ],
#     "error_code": 0
# }

# res = requests.post('https://api.codemao.cn/tiger/accounts/login',
#                     json={
#                         "identity": "18682236985",
#                         "password": "123456",
#                         "pid": "n6kwoCSe"
#                     },
#                     headers={
#                         'content-type': 'application/json'
#                     })
#
# # print(res.text)
# print(jsonpath.jsonpath(res.json(), '$.user_info.id'))

# 利用 jsonpath 解析json
# print jsonpath.jsonpath('', '$.event_list.id')


