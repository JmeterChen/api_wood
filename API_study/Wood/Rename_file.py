#coding=utf-8

import unittest
import requests



class Rename_file(unittest.TestCase):
    """正常重命名线上作品操作"""

    def test_rename_file(self):

        url_login = 'https://api.codemao.cn/tiger/accounts/login'
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

        url = 'https://api.codemao.cn/tiger/work/works/2874829/rename'
        '''将上面获取的cookie加入到请求头'''
        headers['authorization'] = res_cookie
        data = {
            "name": "kobe_bryant",
            "work_type": 7
        }
        res = requests.patch(url=url, headers=headers, json=data)
        self.assertEqual(res.status_code, 200)
        result = res.json()
        self.assertIn('kobe_bryant', result['name'])


    def test_rename_file02(self):
        """作品名重命名为空"""
        url_login = 'https://api.codemao.cn/tiger/accounts/login'
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

        url = 'https://api.codemao.cn/tiger/work/works/2874829/rename'
        '''将上面获取的cookie加入到请求头'''
        headers['authorization'] = res_cookie
        """重命名作品名为空的情况下保存"""
        data = {
            "name": "",
            "work_type": 7
        }
        res = requests.patch(url=url, headers=headers, json=data)
        self.assertEqual(res.status_code, 400)
        result = res.json()
        if result:
            self.assertIn("A_5", result["error_code"])
        else:
            self.assertEqual({}, result)
