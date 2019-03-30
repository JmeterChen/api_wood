# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2018/12/28

import os
import requests
from Methods import json_dict,Parametrized


class Open_file(Parametrized.ParametrizedTestCase):
    """打开云端作品"""

    @classmethod
    def setUpClass(cls):
        cls_name = cls.__name__
        cls.data_dict = (json_dict.json_to_dict(os.path.dirname(os.path.dirname(__file__)) +
                                                '/json_file/wood_data.json'))[cls.env]
        cls.url = cls.data_dict['host'] + cls.data_dict[cls_name]['api']
        cls.headers = cls.data_dict[cls_name]['headers']
        if cls.env == 'pro':
            cls.headers['authorization'] = cls.data_dict['authorization']
        else:
            cls.headers[cls.env + '-authorization'] = cls.data_dict[cls.env + '-authorization']
        cls.work_id = cls.data_dict[cls_name]['work_id']
        cls.response = cls.data_dict[cls_name]['response']
        
    def test_08_open_file01(self):
        """登录态正常-打开存在作品"""
        url = self.url % self.work_id['normal_id']
        res = requests.get(url=url, headers=self.headers)
        result = res.json()
        # 添加断言
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result["name"], self.response["work_name"])

    def test_09_open_file02(self):
        """ 登录态正常-打开已被删除作品"""

        # 该作品已被删除
        url = self.url % self.work_id['deleted_id']
        res = requests.get(url=url, headers=self.headers)
        result = res.json()
        # 添加断言
        self.assertEqual(res.status_code, 410)
        self.assertEqual("W", result["error_category"])

    def test_10_open_file03(self):
        """ 登录态正常-打开未存在过的作品"""

        # 9999999 该作品未生成
        url = self.url % self.work_id['unexist_id']
        res = requests.get(url=url, headers=self.headers)
        result = res.json()
        # 添加断言
        self.assertEqual(res.status_code, 404)
        self.assertEqual("W", result["error_category"])

    def test_11_open_file04(self):
        """登录态正常--打开作品id不符合规则的作品"""

        # adcdefg 该作品id不符合规则
        url = self.url % self.work_id['undefine_id']
        res = requests.get(url=url, headers=self.headers)
        result = res.json()
        # 添加断言
        self.assertEqual(res.status_code, 400)
        self.assertEqual("A",result["error_category"])

    def test_12_open_file05(self):
        """登录态失效--打开作品"""
        headers = self.headers.copy()
        if self.env == 'pro':
            headers['authorization'] = 'abcdefg'
        else:
            headers[self.env + '-authorization'] = 'abcdefg'
        url = self.url % self.work_id['normal_id']
        res = requests.get(url=url, headers=headers)
        result = res.json()
        # 添加断言
        self.assertEqual(res.status_code, 403)
        self.assertEqual("E",result["error_category"])