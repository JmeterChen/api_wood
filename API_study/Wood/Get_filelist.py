#coding=utf-8

import requests
import unittest

class Get_filelist(unittest.TestCase):
    """拉取云端作品列表"""
    def test_get_filelist(self):
        """ 正常数据进行拉取作品列表操作"""
        url_login = 'https://api.maocode.cn/tiger/accounts/login'
        headers = {'Content-Type': 'application/json'}
        data_login = {"identity": "18682236985", "password": "123456", "pid": "n6kwoCSe"}
        res_login = requests.post(url=url_login, headers=headers, json=data_login)
        """这是获取有效cookie """
        res_cookie = res_login.cookies.get('authorization')
        url = 'https://api.maocode.cn/tiger/wood/user/works?'
        '''将上面获取的cookie加入到请求头'''
        headers['authorization'] = res_cookie
        # 正常参数
        para = {
            "page": 1,
            "limit": 15,
            "language_type": 1
        }
        res = requests.get(url=url, params=para, headers=headers)
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


    def test_get_filelist02(self):
        # """ 正常数据进行拉取作品列表操作"""
        # url_login = 'https://api.maocode.cn/tiger/accounts/login'
        headers = {'Content-Type': 'application/json'}
        # data_login = {"identity": "18682236985", "password": "123456", "pid": "n6kwoCSe"}
        # res_login = requests.post(url=url_login, headers=headers, json=data_login)
        # """这是获取有效cookie """
        # res_cookie = res_login.cookies.get('authorization')
        url = 'https://api.maocode.cn/tiger/wood/user/works?'
        # '''模式无效cookie进行拉取作品列表'''
        res_cookie = 'abcdefg'
        headers['authorization'] = res_cookie
        # 正常参数
        para = {
            "page": 1,
            "limit": 15,
            "language_type": 1
        }
        res = requests.get(url=url, params=para, headers=headers)
        self.assertEqual(res.status_code, 403)
        result = res.json()
        # print(type(result))
        if result != []:
            # self.assertIn("work_id", result[0])
            # self.assertIn("name", result[0])
            self.assertEqual('E_1', result['error_code'])
        else:
            self.assertEqual([], result)


