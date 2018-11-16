#coding=utf-8
import unittest
import requests
import json,time

class Delete_file(unittest.TestCase):
    """删除线上作品"""

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
    '''将上面获取的cookie加入到请求头'''
    headers['authorization'] = res_cookie
    url_workid = 'https://api.codemao.cn/tiger/wood/user/works?page=1&limit=15&language_type=0'
    res_workid_list = requests.get(url=url_workid, headers=headers)
    result_workid_list = res_workid_list.json()
    # print(type(result_workid_list))


    def test_21_delete_file01(self):
        """正常登录态-进行删除操作"""
        time.sleep(2)
        url_login = 'https://api.codemao.cn/tiger/accounts/login'
        headers = {'Content-Type': 'application/json'}
        data_login = {"identity": "18682236985","password": "123456","pid": "n6kwoCSe"}
        res_login = requests.post(url=url_login, headers=headers, json=data_login)
        """这是获取有效cookie """
        res_cookie = res_login.cookies.get('authorization')
        # print(res_cookie)
        '''将上面获取的cookie加入到请求头'''
        headers['authorization'] = res_cookie
        url_workid = 'https://api.codemao.cn/tiger/wood/user/works?page=1&limit=15&language_type=0'
        res_workid_list = requests.get(url=url_workid, headers=headers)
        result_workid_list = res_workid_list.json()
        # print(result_workid_list)
        """"""
        if len(result_workid_list) >= 2:
            for i in range(2):
                result_workid = str(result_workid_list[i]["work_id"])
                url = "https://api.codemao.cn/tiger/work/" + result_workid + "/permanently"
                res = requests.delete(url=url, headers=headers)
                self.assertEqual(res.status_code, 204)

        elif len(result_workid_list) == 1:
            result_workid = str(result_workid_list[0]["work_id"])
            url = "https://api.codemao.cn/tiger/work/" + result_workid + "/permanently"
            res = requests.delete(url=url, headers=headers)
            self.assertEqual(res.status_code, 204)
            res_workid_list = requests.get(url=url_workid, headers=headers)
            result_workid_list = res_workid_list.json()
            self.assertEqual(len(result_workid_list), 0)
        else:
            raise ("没有作品可以用来删除！")


    def test_22_delete_file02(self):
        """ 正常登录态- 删除早已删除作品"""
        url = "https://api.codemao.cn/tiger/work/" + '3352256' + "/permanently"
        res = requests.delete(url=url, headers=self.headers)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(res.json()['error_code'],"W_11")


    def test_23_delete_file03(self):
        """ 正常登录态- 删除不存在作品"""
        url = "https://api.codemao.cn/tiger/work/" + '0000000' + "/permanently"
        res = requests.delete(url=url, headers=self.headers)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json()['error_code'],"W_0")


    def test_24_delete_file04(self):
        """ 正常登录态- 删除不符合规则作品"""
        url = "https://api.codemao.cn/tiger/work/" + 'aaaaaaa' + "/permanently"
        res = requests.delete(url=url, headers=self.headers)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['error_code'],"A_5")


    def test_25_delete_file05(self):
        """ 登录态失效- 删除作品"""
        headers = self.headers.copy()
        headers['authorization'] = ""
        url = "https://api.codemao.cn/tiger/work/" + '2287499' + "/permanently"
        res = requests.delete(url=url, headers=headers)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(res.json()['error_code'],"E_0")