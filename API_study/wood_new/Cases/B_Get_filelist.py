# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2018/12/28


import os
import requests
from Methods import json_dict,Parametrized


class Get_filelist(Parametrized.ParametrizedTestCase):
    """拉取云端作品列表"""

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
        cls.para = cls.data_dict[cls_name]['para']

    def test_04_get_filelist01(self):
        """登录态正常--进行拉取作品列表操作"""
        # print(self.url, self.para, self.headers)
        res = requests.get(url=self.url, params=self.para, headers=self.headers)

        self.assertEqual(res.status_code, 200)
        result = res.json()
        # print(type(result[0]["language_type"]))  # int
        # print(type(result))
        if result:
            self.assertIn("work_id", result[0])
            self.assertIn("name", result[0])
            self.assertEqual(1, result[0]["language_type"])
        else:
            self.assertEqual([], result)

    def test_05_get_filelist02(self):
        """登录态失效--拉取作品列表操作"""
        headers = self.headers.copy()
        if self.env == 'pro':
            headers['authorization'] = 'abcdefg'
        else:
            headers[self.env + '-authorization'] = 'abcdefg'
        
        # 发起请求
        res = requests.get(url=self.url, params=self.para, headers=headers)

        # 添加断言
        self.assertEqual(res.status_code, 403)
        result = res.json()
        # print(type(result))
        if result:
            # self.assertIn("work_id", result[0])
            # self.assertIn("name", result[0])
            self.assertEqual('E_1', result['error_code'])
        else:
            self.assertEqual([], result)


