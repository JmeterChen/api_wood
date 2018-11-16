#coding:utf-8
import requests
import unittest
import util

class Register(unittest.TestCase):
    '''登录接口'''


    url = 'http://139.199.132.220:9000/event/api/register/'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    # passwd = util.base64_encode('123huicehuice!@#')
    data = {
            'username': 'huice',
            'password': 'MTIzaHVpY2VodWljZSFAIw=='
        }


    def test_register01(self):

        '''登录正向流程'''
        res = requests.post(url=self.url, headers=self.headers, data=self.data)

        # 添加断言
        print (res.json().get('error_code'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get('error_code'), 0)
        self.assertLess(int(round(res.elapsed.total_seconds()*1000)), 500)


    def test_register02(self):

        '''登录-密码错误'''
        self.data['password'] = 'huicehuice!@#'
        res = requests.post(url=self.url, headers=self.headers, data=self.data)

        # 添加断言
        self.assertEqual(res.status_code, 200)  # 判断两个字是否相等
        self.assertEqual(res.json().get('error_code'), 10000)
        self.assertLess(int(round(res.elapsed.total_seconds() * 1000)), 500)

