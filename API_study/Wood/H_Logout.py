# coding=utf-8
# @Author:ChenBo lin

import unittest
import requests


class Logout(unittest.TestCase):
    """退出登录接口"""


    url_login = 'https://api.codemao.cn/tiger/accounts/login'
    headers = {'Content-Type': 'application/json'}
    data_login = {"identity": "18682236985", "password": "123456", "pid": "n6kwoCSe"}
    res_login = requests.post(url=url_login, headers=headers, json=data_login)
    """这是获取有效cookie """
    res_cookie = res_login.cookies.get('authorization')
    '''将上面获取的cookie加入到请求头'''
    headers['authorization'] = res_cookie


    def test_26_logout(self):
        """ 登录态正常--退出登录操作"""

        url = "https://api.codemao.cn/tiger/accounts/logout"
        res = requests.post(url=url, headers=self.headers)
        self.assertEquals(res.status_code, 204)


    def test_27_logout(self):
        """ 登录态失效--退出登录操作"""

        headers = self.headers.copy()
        headers['authorization'] = ''
        url = "https://api.codemao.cn/tiger/accounts/logout"
        res = requests.post(url=url, headers=headers)
        self.assertEquals(res.status_code, 204)