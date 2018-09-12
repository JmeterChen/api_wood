#coding=utf-8
import requests
import unittest


class Save_file(unittest.TestCase):
    """wood保存接口"""
    def test_save(self):
        """ 正常数据进行保存操作"""
        url_login = 'https://api.codemao.cn/tiger/accounts/login'
        headers = {'Content-Type': 'application/json'}
        data_login = {"identity": "18682236985", "password": "123456", "pid": "n6kwoCSe"}
        res_login = requests.post(url=url_login, headers=headers, json=data_login)
        """这是获取有效cookie """
        res_cookie = res_login.cookies.get('authorization')
        url = 'https://api.codemao.cn/tiger/work/wood'
        '''将上面获取的cookie加入到请求头'''
        headers['authorization'] = res_cookie

        """wood保存接口，正常保存 """
        data = {
            # 作品名称长度 双端做限制
            "name": "API_Test",
            # 作品内容长度 双端做限制
            "content": "def function1():    pass",
            # 作品类型 双端做限制
            "language_type": 1
        }
        res = requests.post(url=url, headers=headers, json=data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get('name')[:8], 'API_Test')

    def test_save02(self):
        """ 使用无效cookie进行保存操作"""
        url_login = 'https://api.codemao.cn/tiger/accounts/login'
        headers = {'Content-Type': 'application/json'}
        data_login = {"identity": "18682236985", "password": "123456", "pid": "n6kwoCSe"}
        res_login = requests.post(url=url_login, headers=headers, json=data_login)
        """这是获取有效cookie """
        res_cookie = res_login.cookies.get('authorization')
        """破坏有效cookie"""
        res_cookie = res_cookie + 'a'
        url = 'https://api.codemao.cn/tiger/work/wood'
        '''将上面获取的无效cookie加入到请求头'''
        headers['authorization'] = res_cookie

        """wood保存接口，正常保存 """
        data = {
            "name": "API_Test",
            "content": "def function1():    pass",
            "language_type": 1
        }
        res = requests.post(url=url, headers=headers, json=data)
        # 因为是无效的cookie，所以返回的状态码应该是401
        self.assertEqual(res.status_code, 401)

    def test_save03(self):
        """ 作品长度为0，进行保存操作"""
        url_login = 'https://api.codemao.cn/tiger/accounts/login'
        headers = {'Content-Type': 'application/json'}
        data_login = {"identity": "18682236985", "password": "123456", "pid": "n6kwoCSe"}
        res_login = requests.post(url=url_login, headers=headers, json=data_login)
        """这是获取有效cookie """
        res_cookie = res_login.cookies.get('authorization')
        url = 'https://api.codemao.cn/tiger/work/wood'
        '''将上面获取的cookie加入到请求头'''
        headers['authorization'] = res_cookie

        """wood保存接口，正常保存 """
        data = {
            # 作品名称长度 双端做限制(及不可以为0，也不可以超过50)
            # len = 0
            "name": "",
            # 作品内容长度 双端做限制
            "content": "def function1():    pass",
            # 作品类型 双端做限制
            "language_type": 1
        }
        res = requests.post(url=url, headers=headers, json=data)
        # 因为请求参数里面有错误的数据，服务器会返回400
        self.assertEqual(res.status_code, 400)

    def test_save04(self):
        """ 作品长度超过限制进行保存操作"""
        url_login = 'https://api.codemao.cn/tiger/accounts/login'
        headers = {'Content-Type': 'application/json'}
        data_login = {"identity": "18682236985", "password": "123456", "pid": "n6kwoCSe"}
        res_login = requests.post(url=url_login, headers=headers, json=data_login)
        """这是获取有效cookie """
        res_cookie = res_login.cookies.get('authorization')
        url = 'https://api.codemao.cn/tiger/work/wood'
        '''将上面获取的cookie加入到请求头'''
        headers['authorization'] = res_cookie

        """wood保存接口，正常保存 """
        data = {
            # 作品名称长度 双端做限制(50>=len>0)
            # len = 51
            "name": "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbn",
            # 作品内容长度 双端做限制
            "content": "def function1():    pass",
            # 作品类型 双端做限制
            "language_type": 1
        }
        res = requests.post(url=url, headers=headers, json=data)
        #因为请求参数里面有错误的数据，服务器会返回400
        self.assertEqual(res.status_code, 400)

    # def test_save05(self):
    #     """ 使用登录接口获取此时登录有效cookie"""
    #     url_login = 'https://api.codemao.cn/tiger/accounts/login'
    #     headers = {'Content-Type': 'application/json'}
    #     data_login = {"identity": "18682236985", "password": "123456", "pid": "n6kwoCSe"}
    #     res_login = requests.post(url=url_login, headers=headers, json=data_login)
    #     """这是获取有效cookie """
    #     res_cookie = res_login.cookies.get('authorization')
    #     url = 'https://api.codemao.cn/tiger/work/wood'
    #     '''将上面获取的cookie加入到请求头'''
    #     headers['authorization'] = res_cookie
    #
    #     """wood保存接口，正常保存 """
    #     data = {
    #         # 作品名称长度 双端做限制(50>=len>0)
    #         "name": "API_Test",
    #         # 作品内容长度 双端做限制 len <= 7500
    #         # 这里(len = 7501)
    #         "content": "",
    #         # 作品类型 双端做限制
    #         "language_type": 1
    #     }
    #     res = requests.post(url=url, headers=headers, json=data)
    #     # 因为请求参数里面有错误的数据，服务器会返回400
    #     self.assertEqual(res.status_code, 400)

    def test_save06(self):
        """ 作品类型为2(硬件作品)进行保存"""
        url_login = 'https://api.codemao.cn/tiger/accounts/login'
        headers = {'Content-Type': 'application/json'}
        data_login = {"identity": "18682236985", "password": "123456", "pid": "n6kwoCSe"}
        res_login = requests.post(url=url_login, headers=headers, json=data_login)
        """这是获取有效cookie """
        res_cookie = res_login.cookies.get('authorization')
        url = 'https://api.codemao.cn/tiger/work/wood'
        '''将上面获取的cookie加入到请求头'''
        headers['authorization'] = res_cookie

        """wood保存接口，正常保存 """
        data = {
            # 作品名称长度 双端做限制(50>=len>0)
            "name": "API_Test",
            # 作品内容长度 双端做限制
            "content": "def function1():    pass",
            # 作品类型 双端做限制
            # 类型为2 为硬件作品，可以正常保存
            "language_type": 2
        }
        res = requests.post(url=url, headers=headers, json=data)
        #因为请求参数里面有错误的数据，服务器会返回400
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get('name')[:10], 'API_Test-1')

    def test_save07(self):
        """ 异常作品类型进行保存操作"""
        url_login = 'https://api.codemao.cn/tiger/accounts/login'
        headers = {'Content-Type': 'application/json'}
        data_login = {"identity": "18682236985", "password": "123456", "pid": "n6kwoCSe"}
        res_login = requests.post(url=url_login, headers=headers, json=data_login)
        """这是获取有效cookie """
        res_cookie = res_login.cookies.get('authorization')
        url = 'https://api.codemao.cn/tiger/work/wood'
        '''将上面获取的cookie加入到请求头'''
        headers['authorization'] = res_cookie

        """wood保存接口，正常保存 """
        data = {
            # 作品名称长度 双端做限制(50>=len>0)
            "name": "API_Test",
            # 作品内容长度 双端做限制
            "content": "def function1():    pass",
            # 作品类型 双端做限制
            # 无效作品数据类型为0
            "language_type": 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        # 因为请求参数里面有错误的数据，服务器会返回400
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json().get('error_category'), "A")
        self.assertEqual(res.json().get('error_number'), 5)
        self.assertEqual(res.json().get('error_code'), "A_5")

