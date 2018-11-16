#coding=utf-8

import requests
import unittest


class Get_filelist(unittest.TestCase):
    """拉取云端作品列表"""
    url_login = 'https://api.codemao.cn/tiger/accounts/login'
    headers = {'Content-Type': 'application/json'}
    data_login = {"identity": "18682236985", "password": "123456", "pid": "n6kwoCSe"}
    res_login = requests.post(url=url_login, headers=headers, json=data_login)
    """这是获取有效cookie """
    res_cookie = res_login.cookies.get('authorization')
    url = 'https://api.codemao.cn/tiger/wood/user/works?'

    # 正常参数
    para = {
        "page": 1,
        "limit": 15,
        "language_type": 1
    }


    def test_04_get_filelist01(self):
        """登录态正常--进行拉取作品列表操作"""

        '''将上面获取的cookie加入到请求头'''
        self.headers['authorization'] = self.res_cookie

        res = requests.get(url=self.url, params=self.para, headers=self.headers)

        self.assertEqual(res.status_code, 200)
        result = res.json()
        # print(type(result[0]["language_type"]))  # int
        # print(type(result))
        if result != []:
            self.assertIn("work_id", result[0])
            self.assertIn("name", result[0])
            self.assertEqual(1, result[0]["language_type"])
        else:
            self.assertEqual([], result)


    def test_05_get_filelist02(self):
        """登录态失效--拉取作品列表操作"""
        headers = self.headers.copy()
        headers['authorization'] = 'abcdefg'
        res = requests.get(url=self.url, params=self.para, headers=headers)

        # 添加断言
        self.assertEqual(res.status_code, 403)
        result = res.json()
        # print(type(result))
        if result != []:
            # self.assertIn("work_id", result[0])
            # self.assertIn("name", result[0])
            self.assertEqual('E_1', result['error_code'])
        else:
            self.assertEqual([], result)


