# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2018/12/28


import os,time
import requests
import unittest
from Methods import json_dict,Parametrized


class Logout(Parametrized.ParametrizedTestCase):
    """退出登录接口"""
    
    @classmethod
    def setUpClass(cls):
        cls_name = cls.__name__
        cls.data_dict = (json_dict.json_to_dict(os.path.dirname(os.path.dirname(__file__)) + \
                                                '/json_file/wood_data.json'))[cls.env]
        cls.url = cls.data_dict['host'] + cls.data_dict[cls_name]['api']
        cls.headers = cls.data_dict[cls_name]['headers']
        if cls.env == 'pro':
            cls.headers['authorization'] = cls.data_dict['authorization']
        else:
            cls.headers[cls.env + '-authorization'] = cls.data_dict[cls.env + '-authorization']

    def test_26_logout01(self):
        """ 登录态正常--退出登录操作"""
        res = requests.post(url=self.url, headers=self.headers)
        self.assertEquals(res.status_code, 204)

    def test_27_logout02(self):
        """ 登录态失效--退出登录操作"""

        headers = self.headers.copy()
        if self.env == 'pro':
            headers['authorization'] = ''
        else:
            headers[self.env + '-authorization'] = ''
        res = requests.post(url=self.url, headers=headers)
        self.assertEquals(res.status_code, 204)