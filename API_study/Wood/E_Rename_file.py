#coding=utf-8

import unittest
import requests
import util,time

class Rename_file(unittest.TestCase):
    """重命名线上作品操作"""

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
    # print(res_cookie)

    url = 'https://api.maocode.cn/tiger/work/works/2598407/rename'
    '''将上面获取的cookie加入到请求头'''
    headers['authorization'] = res_cookie
    data = {
        "name": "kobe_bryant",
        "work_type": 7
    }


    def test_13_rename_file01(self):
        """登录态正常--重命名为一个新的作品"""
        time.sleep(0.5)
        data = self.data.copy()
        data['name'] += util.create_num()
        # print(data)
        res = requests.patch(url=self.url, headers=self.headers, json=data)

        # 添加断言
        self.assertEqual(res.status_code, 200)
        result = res.json()
        self.assertIn(data['name'], result['name'])


    def test_14_rename_file02(self):
        """登录态正常--作品名重命名为空"""
        data = self.data.copy()
        data['name'] = ''
        res = requests.patch(url=self.url, headers=self.headers, json=data)
        self.assertEqual(res.status_code, 400)
        result = res.json()
        if result:
            self.assertIn("A_5", result["error_code"])
        else:
            self.assertEqual({}, result)


    def test_15_rename_file03(self):
        """登录态失效--进行重命名操作"""
        headers = self.headers.copy()
        headers['authorization'] = ''
        res = requests.patch(url=self.url, headers=headers,json=self.data,)
        # 添加断言
        self.assertEqual(res.status_code, 403)
        result = res.json()
        self.assertEqual(result["error_code"], "E_0")