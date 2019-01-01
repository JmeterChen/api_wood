# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2018/12/28

# from API_study.New_wood2.Cases import A_Login

from Cases import A_Login
import unittest
import HTMLTestRunnerCN
import sys, time, os


if __name__ == '__main__':
    # 方式1：控制单条用例执行
    tmp = os.sep
    suite = unittest.TestSuite()
    # suite.addTest(A_Login.Login('test_01_wood_login01'))
    
    # suite.addTest(G_Delete_file.Delete_file('test_26_delete_file06'))
    
    # 方式2：通过正则搜索添加用例
    
    suite = unittest.defaultTestLoader.discover(start_dir=os.getcwd() + tmp + 'Cases', pattern='*.py')
    # # print(len(suite._tests))
    # # py2
    # HTMLTestRunnerCN.HTMLTestRunner(stream=open(os.getcwd() + tmp + 'Output\\report.html', 'wb'),\
    # 				title='Wood_API', description='WoodAPI_demo', tester='Bo_lin Chen').run(suite)
    HTMLTestRunnerCN.HTMLTestRunner(stream=open(os.getcwd() + tmp + 'Output' + tmp +'report.html', 'wb'),\
                    title='Wood_API', description='WoodAPI_demo', tester='Bo_lin Chen').run(suite)
