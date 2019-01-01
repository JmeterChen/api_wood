# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2018/12/28

import os,time
import requests
import unittest
from Methods import json_dict


class Delete_file(unittest.TestCase):
    """删除线上作品"""
    
    @classmethod
    def setUpClass(cls):
        cls_name = cls.__name__
        cls.data_dict = (json_dict.json_to_dict(os.path.dirname(os.path.dirname(__file__)) + \
                                                '/json_file/wood_data.json'))['pro']
        cls.url = cls.data_dict['host'] + cls.data_dict[cls_name]['api']
        cls.headers = cls.data_dict[cls_name]['headers']
        cls.headers['authorization'] = cls.data_dict['authorization']
        cls.work_id_py = cls.data_dict['work_id_py']
        cls.work_id_hex = cls.data_dict['work_id_hex']

    def test_21_delete_file01(self):
        """正常登录态- 删除Python类型作品"""
        time.sleep(3)
        url = self.url % self.work_id_py
        print("test_21_delete_file01 :", url)
        res = requests.delete(url=url, headers=self.headers)
        self.assertEqual(res.status_code, 204)
        
    def test_22_delete_file02(self):
        """正常登录态- 删除hex类型作品"""
        url = self.url % self.work_id_hex
        print("work_id_hexwork_id_hex:", url)
        res = requests.delete(url=url, headers=self.headers)
        self.assertEqual(res.status_code, 204)

    def test_23_delete_file03(self):
        """ 正常登录态- 删除早已删除作品"""
        url = self.url % self.work_id_py
        res = requests.delete(url=url, headers=self.headers)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(res.json()['error_code'], "W_11")

    def test_24_delete_file04(self):
        """ 正常登录态- 删除不存在作品"""
        work_id = '0000000'
        url = self.url % work_id
        res = requests.delete(url=url, headers=self.headers)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json()['error_code'], "W_0")

    def test_25_delete_file05(self):
        """ 正常登录态- 删除不符合规则作品"""
        work_id = 'aaaaaaa'
        url = self.url % work_id
        res = requests.delete(url=url, headers=self.headers)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['error_code'],"A_5")

    def test_26_delete_file06(self):
        """ 登录态失效- 删除作品"""
        headers = self.headers.copy()
        headers['authorization'] = ""
        url = self.url % self.work_id_hex
        res = requests.delete(url=url, headers=headers)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(res.json()['error_code'],"E_0")
