#coding:utf-8
import requests
import json

url = 'https://api.codemao.cn/tiger/accounts/login'
headers = {'Content-Type': 'application/json'}
data = {"identity": "18682236985",
        "password": "123456",
        "pid": "n6kwoCSe"
        }
res = requests.post(url=url, headers=headers, json=data)
res_cookie = res.cookies.get('authorization')
print(type(res_cookie))

#1 测试get请求
# res = requests.get(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString?theRegionCode=3117')
# print res.status_code
# print res.text

#2 动态拼接请参数 get
# params = {'theRegionCode': '3117'}
# res = requests.get(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString', params=params)
# print res.status_code
# print res.text

#3 post请求 url-encode
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# data = {'theRegionCode': '3117'}
# res = requests.post(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString', headers=headers, data=data)
# print res.status_code
# print res.text

#4 post请求 正文是xml soap协议
# headers = {'Content-Type': 'text/xml'}
# data = '''<?xml version="1.0" encoding="utf-8"?>
# <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <getSupportCityString xmlns="http://WebXml.com.cn/">
#       <theRegionCode>3117</theRegionCode>
#     </getSupportCityString>
#   </soap:Body>
# </soap:Envelope>'''
# res = requests.post(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx', headers=headers, data=data)
# print res.status_code
# print res.text

#5 post请求 正文json
# headers = {'Content-Type': 'application/json'}
# data = {"theCityCode": 1}
# res = requests.post(url='http://139.199.132.220:9000/event/weather/getWeather/', headers=headers, data=json.dumps(data))
# print res.status_code
# print res.text

#6 post请求 正文json(二)
# headers = {'Content-Type': 'application/json'}
# data = {"theCityCode": 1}
# res = requests.post(url='http://139.199.132.220:9000/event/weather/getWeather/', headers=headers, json=data)
# print res.status_code
# print res.text

