#coding:utf-8
import requests
import unittest
import util

class Register(unittest.TestCase):
    '''登录接口'''
    def test_register01(self):
        '''登录正向流程'''
        url = 'http://139.199.132.220:9000/event/api/register/'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        data = {
            'username': 'huice',
            'password': util.base64_encode('123huicehuice!@#')
        }
        res = requests.post(url=url, headers=headers, data=data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get('error_code'), 0)
        self.assertLess(int(round(res.elapsed.total_seconds()*1000)), 500)

    def test_register02(self):
        '''登录-密码错误'''
        url = 'http://139.199.132.220:9000/event/api/register/'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        data = {
            'username': 'huice',
            'password': util.base64_encode('huicehuice!@#')
        }
        res = requests.post(url=url,
                      headers=headers,
                      data=data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get('error_code'), 10000)
        self.assertLess(int(round(res.elapsed.total_seconds() * 1000)), 500)