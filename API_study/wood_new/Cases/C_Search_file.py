# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2018/12/28

import os
import requests
from Methods import json_dict,Parametrized


class Search_file(Parametrized.ParametrizedTestCase):
    """搜索云端作品"""

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
        
    def test_06_search_file01(self):
        """登录态正常--进行作品搜索"""
        res = requests.get(url=self.url, params=self.para, headers=self.headers)
        result = res.json()
        print(result)
        self.assertEqual(res.status_code, 200)
        if len(result) == 1:
            self.assertIn("进度条", result[0]["name"])
            self.assertEqual(1, result[0]["language_type"])
        elif len(result) > 1:
            self.assertIn("work_id", result[0])
            self.assertIn("name", result[0])
            self.assertEqual(1, result[0]["language_type"])
        else:
            self.assertEqual([], result)
            
    def test_07_search_file02(self):
        """登录态失效--进行作品搜搜"""
        headers = self.headers.copy()
        if self.env == 'pro':
            headers['authorization'] = 'abcdefg'
        else:
            headers[self.env + '-authorization'] = 'abcdefg'
        res = requests.get(url=self.url, params=self.para, headers=headers)
        result = res.json()
        # 添加断言
        self.assertEqual(res.status_code, 403)
        self.assertEqual("E",result["error_category"])
