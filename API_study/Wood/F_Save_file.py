#coding=utf-8
import requests
import unittest,time


class Save_file(unittest.TestCase):
    """保存作品"""

    url_login = 'https://api.maocode.cn/tiger/accounts/login'
    headers = {'Content-Type': 'application/json'}
    data_login = {"identity": "18682236985", "password": "123456", "pid": "n6kwoCSe"}
    res_login = requests.post(url=url_login, headers=headers, json=data_login)
    """这是获取有效cookie """
    res_cookie = res_login.cookies.get('authorization')
    url = 'https://api.maocode.cn/tiger/work/wood'
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


    def test_15_save01(self):
        """登录态正常--正常保存操作"""
        time.sleep(0.5)
        res = requests.post(url=self.url, headers=self.headers, json=self.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get('name')[:8], 'API_Test')
        # print('ok')



    def test_16_save02(self):
        """登录态失效--进行保存操作"""
        headers = self.headers.copy()  # 这步很重要，没有这步，其他的用例cookie均会被破坏
        headers['authorization'] = 'abcdefg'
        res = requests.post(url=self.url, headers=headers, json=self.data)
        result = res.json()
        # 因为是无效的cookie，所以返回的状态码应该是401
        self.assertEqual(res.status_code, 403)
        self.assertEqual("E",result["error_category"])


    def test_17_save03(self):
        """登录态正常--作品名称长度为0，进行保存操作"""
        # print(self.headers)
        data = self.data.copy()
        data['name'] = ""
        res = requests.post(url=self.url, headers=self.headers, json=data)
        result = res.json()
        # 因为请求参数里面有错误的数据，服务器会返回400
        self.assertEqual(res.status_code, 400)
        self.assertEqual("A",result["error_category"])


    def test_18_save04(self):
        """登录态正常--作品长度超过限制进行保存操作"""
        data = self.data.copy()
        data['name'] = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbn"
        res = requests.post(url=self.url, headers=self.headers, json=data)
        result = res.json()
        #因为请求参数里面有错误的数据，服务器会返回400
        self.assertEqual(res.status_code, 400)
        self.assertEqual("A_5",result["error_code"])

    # def test_save05(self):
    #     """ 使用登录接口获取此时登录有效cookie"""
    #     url_login = 'https://api.maocode.cn/tiger/accounts/login'
    #     headers = {'Content-Type': 'application/json'}
    #     data_login = {"identity": "18682236985", "password": "123456", "pid": "n6kwoCSe"}
    #     res_login = requests.post(url=url_login, headers=headers, json=data_login)
    #     """这是获取有效cookie """
    #     res_cookie = res_login.cookies.get('authorization')
    #     url = 'https://api.maocode.cn/tiger/work/wood'
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

    def test_19_save05(self):
        """登录态正常--作品类型为2(硬件作品)进行保存"""
        time.sleep(0.5)
        data = self.data.copy()
        data['language_type'] = 2
        # print(self.url,self.headers,self.data)
        time.sleep(1.5)
        res = requests.post(url=self.url, headers=self.headers, json=data)
        # print(res)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get('name')[:10], 'API_Test-1')


    def test_20_save06(self):
        """登录态正常--异常作品类型进行保存操作"""
        data = self.data.copy()
        data['language_type'] = 0
        res = requests.post(url=self.url, headers=self.headers, json=data)
        result = res.json()
        # 因为请求参数里面有错误的数据，服务器会返回400
        self.assertEqual(res.status_code, 400)
        self.assertEqual(result.get('error_code'), "A_5")
