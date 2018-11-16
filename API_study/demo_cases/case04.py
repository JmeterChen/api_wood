# coding:utf-8
import requests
import base64
import json
import util,sys
import unittest

reload(sys) 
sys.setdefaultencoding( "utf-8" )


# # demo
# url = 'http://139.199.132.220:9000/event/api/get_eventdetail/'
# headers = {
# 	'Content-Type': 'application/x-www-form-urlencoded',  
# 	'Cookie': 'token=75ff30521dd7bafb48e07cf7e0a0b564dd8896a4;uid=1'
# 	}

# data = {
#     'id': '5713'
# }

# sign = util.create_sign('75ff30521dd7bafb48e07cf7e0a0b564dd8896a4', data)
# data['sign'] = sign


# res = requests.get(url=url, headers=headers, params=data)

# print res.status_code
# print res.text


class Case04(unittest.TestCase):

	def test_case04(self):

		url = 'http://139.199.132.220:9000/event/api/get_eventdetail/'
		headers = {
			'Content-Type': 'application/x-www-form-urlencoded', 
			'Cookie': 'token=75ff30521dd7bafb48e07cf7e0a0b564dd8896a4;uid=1'
			}

		data = {
		    'id': '5713'
		}

		sign = util.create_sign('75ff30521dd7bafb48e07cf7e0a0b564dd8896a4', data)
		data['sign'] = sign


		res = requests.get(url=url, headers=headers, params=data)

		print res.status_code
		print res.text