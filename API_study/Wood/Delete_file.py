#coding=utf-8
import unittest
import requests


class Delete_file(unittest.TestCase):
    """删除线上作品"""
    def test_delete_file(self):
        """正常重命名线上作品操作"""
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
        url_workid = 'https://api.codemao.cn/tiger/wood/user/works?page=1&limit=15&language_type=1'
        res_workid_list = requests.get(url=url_workid, headers=headers)
        result_workid_list = res_workid_list.json()
        # print(result_workid)
        """"""
        if len(result_workid_list) >= 2:
            result_workid = str(result_workid_list[0]["work_id"])
            result_workid_second = (result_workid_list[1]["work_id"])
            url = "https://api.codemao.cn/tiger/work/" + result_workid + "/permanently"
            res = requests.delete(url=url, headers=headers)
            self.assertEqual(res.status_code, 204)

            res_workid_list = requests.get(url=url_workid, headers=headers)
            result_workid_list = res_workid_list.json()
            self.assertEqual(result_workid_list[0]["work_id"], result_workid_second)
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

