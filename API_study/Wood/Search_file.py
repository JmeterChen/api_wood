#coding=utf-8
import requests
import unittest

class Search_file(unittest.TestCase):
    """搜索云端作品"""

    def test_search_file(self):
        """正常登录-账号密码正确"""
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

        url = 'https://api.codemao.cn/tiger/wood/user/works/search?'
        para = {
            "query": "b-2",
            "language_type": 1,
            "page": 1,
            "limit": 15
        }
        '''将上面获取的cookie加入到请求头'''
        headers['authorization'] = res_cookie
        res = requests.get(url=url, params=para, headers=headers)
        result = res.json()
        # print(result)
        self.assertEqual(res.status_code, 200)
        if len(result) == 1:
            self.assertIn(1840892, result[0]["work_id"])
            self.assertIn("b-2222", result[0]["name"])
            self.assertEqual(1, result[0]["language_type"])
        elif len(result) > 1:
            self.assertIn("work_id", result[0])
            self.assertIn("name", result[0])
            self.assertEqual(1, result[0]["language_type"])
        else:
            self.assertEqual([], result)
