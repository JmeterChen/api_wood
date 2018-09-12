#coding=utf-8
import requests
import unittest

class Open_file(unittest.TestCase):

    """先调用wood登录接口"""
    def test_open_file(self):
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

        url = 'https://api.codemao.cn/tiger/wood/works/1840892'
        '''将上面获取的cookie加入到请求头'''
        headers['authorization'] = res_cookie
        res = requests.get(url=url, headers=headers)
        result = res.json()
        print(type(result))
        # self.assertEqual(res.status_code, 200)
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual("b-2", result["name"])

