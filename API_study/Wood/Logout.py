# coding=utf-8
# @Author:ChenBo lin

import unittest
import requests


class Logout(unittest.TestCase):
    """退出登录接口"""

    def test_logout(self):
        url_login = 'https://api.codemao.cn/tiger/accounts/login'
        headers = {'Content-Type': 'application/json'}
        data_login = {"identity": "18682236985", "password": "123456", "pid": "n6kwoCSe"}
        res_login = requests.post(url=url_login, headers=headers, json=data_login)
        """这是获取有效cookie """
        res_cookie = res_login.cookies.get('authorization')
        '''将上面获取的cookie加入到请求头'''
        headers['authorization'] = res_cookie

        url = "https://api.codemao.cn/tiger/accounts/logout"
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url=url, headers=headers)
        self.assertEquals(res.status_code, 204)