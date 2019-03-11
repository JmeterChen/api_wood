# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2018/12/28

import os
import requests
import unittest
# from API_study.New_wood2.Methods import json_dict
from Methods import json_dict,Parametrized


class Login(Parametrized.ParametrizedTestCase):
    """wood登录接口"""

    @classmethod
    def setUpClass(cls):
        cls_name = cls.__name__
        cls.data_dict = json_dict.json_to_dict(os.path.dirname(os.path.dirname(__file__)) + '/json_file/wood_data.json')
        cls.url = cls.data_dict[cls.env]['host'] + cls.data_dict[cls.env][cls_name]['api']
        cls.headers = cls.data_dict[cls.env][cls_name]['headers'].copy()
        cls.data = cls.data_dict[cls.env][cls_name]['data']
        cls.response = cls.data_dict[cls.env][cls_name]['response']
    
    def test_01_wood_login01(self):
        """正常登录-账号密码正确"""
        
        res = requests.post(url=self.url, headers=self.headers, json=self.data)
        # 添加断言
        self.assertEquals(res.status_code, 200)
        self.assertEqual(res.json().get('user_info').get('id'), self.response['id'])
        self.assertEqual(res.json().get('user_info').get('nickname'), self.response['nickname'])
        # a = res.cookies.get('authorization')
        if self.env == 'pro':
            self.data_dict[self.env]['authorization'] = res.cookies.get('authorization')
        elif self.env == 'staging':
            self.data_dict[self.env]['staging-authorization'] = res.cookies.get('staging-authorization')
        elif self.env == 'dev':
            self.data_dict[self.env]['dev-authorization'] = res.cookies.get('dev-authorization')
        elif self.env == 'test':
            self.data_dict[self.env]['test-authorization'] = res.cookies.get('test-authorization')
        else:
            print('请选择正确的环境地址！')
        # print(self.data_dict)
        json_dict.wirte_to_json(os.path.dirname(os.path.dirname(__file__)) + '/json_file/wood_data.json', self.data_dict)

    def test_02_wood_login02(self):

        """异常登录-账号/密码为空"""
        data = self.data.copy()
        data['identity'] = ''
        res = requests.post(url=self.url, headers=self.headers, json=data)

        # 添加断言
        self.assertEquals(res.status_code, 400)
        self.assertEqual(res.json().get('error_category'), 'A')
        self.assertEqual(res.json().get('error_number'), 5)
        self.assertEqual(res.json().get('error_code'), 'A_5')

    def test_03_wood_login03(self):

        """异常登录-账号/密码错误"""
        data = self.data.copy()
        data["password"] = "654321"
        res = requests.post(url=self.url, headers=self.headers, json=data)

        # 添加断言
        self.assertEquals(res.status_code, 403)
        self.assertEqual(res.json().get('error_category'), 'AC')
        self.assertEqual(res.json().get('error_number'), 1)
        self.assertEqual(res.json().get('error_code'), 'AC_1')

