#coding=utf-8
import requests
import unittest


class Login(unittest.TestCase):
    """wood登录接口"""

    url = 'https://api.codemao.cn/tiger/accounts/login'
    headers = {'Content-Type': 'application/json'}
    data = {
            "identity": "18682236985",
            "password": "123456",
            "pid": "n6kwoCSe"
            }


    def test_01_wood_login01(self):
        """正常登录-账号密码正确"""

        res = requests.post(url=self.url, headers=self.headers, json=self.data)

        # 添加断言
        self.assertEquals(res.status_code, 200)
        self.assertEqual(res.json().get('user_info').get('id'), 378392)
        self.assertEqual(res.json().get('user_info').get('nickname'), "陈柏霖")


    def test_02_wood_login02(self):

        """异常登录-账号/密码为空"""
        data = self.data.copy()
        data['identity'] = ''
        res = requests.post(url=self.url, headers=self.headers, json=data)

        # 添加断言
        self.assertEquals(res.status_code, 400)
        self.assertEqual(res.json().get('error_category'), 'A')
        self.assertEqual(res.json().get('error_number'), 5)
        self.assertEqual(res.json().get('error_code'), 'A_5')


    def test_03_wood_login03(self):

        """异常登录-账号/密码错误"""
        data = self.data.copy()
        data["password"] = "654321"
        res = requests.post(url=self.url, headers=self.headers, json=data)

        # 添加断言
        self.assertEquals(res.status_code, 403)
        self.assertEqual(res.json().get('error_category'), 'AC')
        self.assertEqual(res.json().get('error_number'), 1)
        self.assertEqual(res.json().get('error_code'), 'AC_1')