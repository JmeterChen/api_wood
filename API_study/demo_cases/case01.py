#coding:utf-8
import requests
import base64
import json
import util
import unittest

# # demo1 

# url='http://139.199.132.220:9000/event/api/register/'
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# data = {
# 	'username':'huice', 
# 	'password': util.base64_encode('huicehuice!@#')
# 	}

# res = requests.post(url=url,headers=headers,data=data)

# print res.status_code
# print res.text
# # print json.loads(res.text).get('token')  # 等价于 print json.loads(res.text)['token']



# 用例成品
class Case01(unittest.TestCase):

	def test_case01(self):

		url='http://139.199.132.220:9000/event/api/register/'
		headers = {'Content-Type': 'application/x-www-form-urlencoded'}
		data = {
			'username':'huice', 
			'password': util.base64_encode('huicehuice!@#')
			}

		res = requests.post(url=url,headers=headers,data=data)

		print res.status_code
		print res.text


	def test_case02(self):

		print 222