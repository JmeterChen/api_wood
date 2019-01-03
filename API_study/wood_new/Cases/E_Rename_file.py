# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2018/12/28

import os
import requests
import unittest
from Methods import json_dict,Parametrized
import util, time


class Rename_file(Parametrized.ParametrizedTestCase):
    """重命名线上作品操作"""

    @classmethod
    def setUpClass(cls):
        cls_name = cls.__name__
        cls.data_dict = (json_dict.json_to_dict(os.path.dirname(os.path.dirname(__file__)) + \
                                                '/json_file/wood_data.json'))[cls.env]
        cls.url = (cls.data_dict['host'] + cls.data_dict[cls_name]['api']) % cls.data_dict[cls_name]['work_id']
        cls.headers = cls.data_dict[cls_name]['headers']
        if cls.env == 'pro':
            cls.headers['authorization'] = cls.data_dict['authorization']
        else:
            cls.headers[cls.env + '-authorization'] = cls.data_dict[cls.env + '-authorization']
        cls.data = cls.data_dict[cls_name]['data']
        
    def test_13_rename_file01(self):
        """登录态正常--重命名为一个新的作品"""
        
        time.sleep(0.5)
        data = self.data.copy()
        data['name'] += util.create_str(5)
        
        res = requests.patch(url=self.url, headers=self.headers, json=data)

        # 添加断言
        self.assertEqual(res.status_code, 200)
        result = res.json()
        self.assertIn(data['name'], result['name'])

    def test_14_rename_file02(self):
        """登录态正常--作品名重命名为空"""
        
        data = self.data.copy()
        data['name'] = ''
        
        res = requests.patch(url=self.url, headers=self.headers, json=data)
        
        # 添加断言
        self.assertEqual(res.status_code, 400)
        result = res.json()
        if result:
            self.assertIn("A_5", result["error_code"])
        else:
            self.assertEqual({}, result)

    def test_15_rename_file03(self):
        """登录态失效--进行重命名操作"""
        
        headers = self.headers.copy()
        if self.env == 'pro':
            headers['authorization'] = ''
        else:
            headers[self.env + '-authorization'] = ''
        
        res = requests.patch(url=self.url, headers=headers, json=self.data)
        
        # 添加断言
        self.assertEqual(res.status_code, 403)
        result = res.json()
        self.assertEqual(result["error_code"], "E_0")