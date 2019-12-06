#coding=utf-8
import requests
import unittest

class Search_file(unittest.TestCase):
    """搜索云端作品"""

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
    url = 'https://api.maocode.cn/tiger/wood/user/works/search?'
    para = {
        "query": "b-2",
        "language_type": 1,
        "page": 1,
        "limit": 15
    }
    '''将上面获取的cookie加入到请求头'''
    headers['authorization'] = res_cookie


    def test_06_search_file01(self):
        """登录态正常--进行作品搜索"""
        res = requests.get(url=self.url, params=self.para, headers=self.headers)
        result = res.json()
        # print(result)
        self.assertEqual(res.status_code, 200)
        if len(result) == 1:
            self.assertIn("b-2", result[0]["name"])
            self.assertEqual(1, result[0]["language_type"])
        elif len(result) > 1:
            self.assertIn("work_id", result[0])
            self.assertIn("name", result[0])
            self.assertEqual(1, result[0]["language_type"])
        else:
            self.assertEqual([], result)


    def test_07_search_file02(self):
        """登录态失效--进行作品搜搜"""
        headers = self.headers.copy()
        headers['authorization'] = 'abcdefg'
        res = requests.get(url=self.url, params=self.para, headers=headers)
        result = res.json()
        # 添加断言
        self.assertEqual(res.status_code, 403)
        self.assertEqual("E",result["error_category"])
