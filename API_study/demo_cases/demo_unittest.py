# coding:utf-8
import requests
import base64
import json
import util,sys
import unittest

reload(sys) 
sys.setdefaultencoding( "utf-8" )


class MyTest(unittest.TestCase):


	def test_case1(self):

		# print 1
		url='http://139.199.132.220:9000/event/api/register/'
		headers = {'Content-Type': 'application/x-www-form-urlencoded'}
		data = {
			'username':'huice', 
			'password': util.base64_encode('huicehuice!@#')
			}

		res = requests.post(url=url,headers=headers,data=data)

		print res.status_code
		print res.text



	def test_case2(self):

		# print 2
		url='http://139.199.132.220:9000/event/api/register/'
		headers = {'Content-Type': 'application/x-www-form-urlencoded'}
		data = {
			'username':'huice', 
			'password': util.base64_encode('huicehuice!@#')
			}

		res = requests.post(url=url,headers=headers,data=data)

		print res.status_code
		print res.text


	def test_case3(self):

		# print 3
		url = 'http://139.199.132.220:9000/event/api/add_event/'
		headers = {
			'Content-Type': 'application/x-www-form-urlencoded', 
			'Cookie': 'token=75ff30521dd7bafb48e07cf7e0a0b564dd8896a4;uid=1'
			}

		data = {
		    'title': '慧测接口测试02',
		    'time': '2018-09-01 15:00:00',
		    'address': '汤立路220号1号楼007',
		}

		sign = util.create_sign('75ff30521dd7bafb48e07cf7e0a0b564dd8896a4', data)
		data['sign'] = sign


		res = requests.post(url=url, headers=headers, data=data)

		print res.status_code
		print res.text


	def test_case4(self):

		# print 4
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


if __name__ == '__main__':
	unittest.main()