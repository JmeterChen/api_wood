#coding=utf-8
import requests
import unittest

class Login(unittest.TestCase):
    """wood登录接口"""
    def test_wood_login(self):
        """正常登录-账号密码正确"""
        url = 'https://api.codemao.cn/tiger/accounts/login'
        headers = {'Content-Type': 'application/json'}
        data = {
                "identity": "18682236985",
                "password": "123456",
                "pid": "n6kwoCSe"
                }
        res = requests.post(url=url, headers=headers, json=data)
        self.assertEquals(res.status_code, 200)
        self.assertEqual(res.json().get('user_info').get('id'), 378392)
        self.assertEqual(res.json().get('user_info').get('nickname'), "陈柏霖")


    def test_wood_login02(self):
        """异常登录-账号/密码为空"""
        url = 'https://api.codemao.cn/tiger/accounts/login'
        headers = {'Content-Type': 'application/json'}
        data = {
                "identity": "",
                "password": "123456",
                "pid": "n6kwoCSe"
                }
        res = requests.post(url=url, headers=headers, json=data)
        self.assertEquals(res.status_code, 400)
        self.assertEqual(res.json().get('error_category'), 'A')
        self.assertEqual(res.json().get('error_number'), 5)
        self.assertEqual(res.json().get('error_code'), 'A_5')

    def test_wood_login03(self):
        """异常登录-账号/密码错误"""
        url = 'https://api.codemao.cn/tiger/accounts/login'
        headers = {'Content-Type': 'application/json'}
        data = {
                "identity": "18682236985",
                "password": "654321",
                "pid": "n6kwoCSe"
                }
        res = requests.post(url=url, headers=headers, json=data)
        self.assertEquals(res.status_code, 403)
        self.assertEqual(res.json().get('error_category'), 'AC')
        self.assertEqual(res.json().get('error_number'), 1)
        self.assertEqual(res.json().get('error_code'), 'AC_1')