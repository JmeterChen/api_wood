# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2018/12/28

import unittest
import json


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        # print("testnames: ",testnames)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite


# 给定json数据路径 读取json并返回字典
def json_to_dict(path):
    with open(path, 'r', encoding='utf-8') as jp:
        data = json.loads(jp.read())
        return data


# 将两个字典合并为一个
def merge_dict(data1, data2):
    data3 = data1.copy()
    data3.update(data2)
    return data3


# 将字典数据与json数据'合并'写入json文件
def data_to_json(path, data):
    data_json = json_to_dict(path)
    data_dict = merge_dict(data_json, data)
    with open(path, 'w') as f:
        json.dump(data_dict, f, indent=4)
        f.flush()


# 将字典数据直接以覆盖的方式写入json文件
def wirte_to_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        f.flush()


a = {'name': 'kobe'}

# 验证字典与json'合并'
# data_to_json(a, 'json_data_test.jB_Get_filelistson')

# 验证字典覆盖写入json
if __name__ == '__main__':
    wirte_to_json(a, 'json_data_test2.json')