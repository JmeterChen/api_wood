#coding=utf-8
import requests
import unittest

class Open_file(unittest.TestCase):
    """打开云端作品"""

    url_login = 'https://api.maocode.cn/tiger/accounts/login'
    headers = {'Content-Type': 'application/json'}
    data_login = {
            "identity": "18682236985",
            "password": "123456",
            "pid": "n6kwoCSe"
            }
    res_login = requests.post(url=url_login, headers=headers, json=data_login)
    """这是获取有效cookie """
    res_cookie = res_login.cookies.get('authorization')

    url = 'https://api.maocode.cn/tiger/wood/works/4255288'  # 小猪佩奇
    '''将上面获取的cookie加入到请求头'''
    headers['authorization'] = res_cookie

    def test_08_open_file01(self):
        """正常登录态-打开存在作品"""

        res = requests.get(url=self.url, headers=self.headers)
        result = res.json()
        # 添加断言
        self.assertEqual(res.status_code, 200)
        self.assertEqual(u"小猪佩奇", result["name"])


    def test_09_open_file02(self):
        """ 正常登录态-打开已被删除作品"""

        # 3352256 该作品已被删除
        self.url = 'https://api.maocode.cn/tiger/wood/works/3352256'
        res = requests.get(url=self.url, headers=self.headers)
        result = res.json()
        # 添加断言
        self.assertEqual(res.status_code, 410)
        self.assertEqual("W",result["error_category"])


    def test_10_open_file03(self):
        """登录态正常-打开未存在过的作品"""

        # 9999999 该作品未生成
        self.url = 'https://api.maocode.cn/tiger/wood/works/9999999'
        res = requests.get(url=self.url, headers=self.headers)
        result = res.json()
        # 添加断言
        self.assertEqual(res.status_code, 404)
        self.assertEqual("W",result["error_category"])


    def test_11_open_file04(self):
        """登录态正常--打开作品id不符合规则的作品"""

        # adcdefg 该作品id不符合规则
        self.url = 'https://api.maocode.cn/tiger/wood/works/adcdefg'
        res = requests.get(url=self.url, headers=self.headers)
        result = res.json()
        # 添加断言
        self.assertEqual(res.status_code, 400)
        self.assertEqual("A",result["error_category"]) 


    def test_12_open_file05(self):
        """登录态失效--打开作品"""
        headers = self.headers.copy()
        headers['authorization'] = 'abcdefg'
        self.url = 'https://api.maocode.cn/tiger/wood/works/1840852'
        res = requests.get(url=self.url, headers=headers)
        result = res.json()
        # 添加断言
        self.assertEqual(res.status_code, 403)
        self.assertEqual("E",result["error_category"])