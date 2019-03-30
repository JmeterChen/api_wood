# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2018/12/28

# from API_study.New_wood2.Cases import A_Login

# from Cases import A_Login,E_Rename_file,F_Save_file
import unittest
import HTMLTestReportCN
import sys, time, os
from collections import Iterable
from Methods import Parametrized


if __name__ == '__main__':
    # 方式1：控制单条用例执行
    tmp = os.sep
    # suite = unittest.TestSuite()
    # suite.addTest(A_Login.Login('test_01_wood_login01'))
    # suite.addTest(E_Rename_file.Rename_file('test_13_rename_file01'))
    # suite.addTest(F_Save_file.Save_file('test_15_save01'))
    
    # suite.addTest(G_Delete_file.Delete_file('test_26_delete_file06'))
    
    # 方式2：通过case文件名指定接口测试
    # suite = unittest.defaultTestLoader.discover(start_dir=os.getcwd() + tmp + 'Cases', pattern='A_Login.py')
    # suite = unittest.defaultTestLoader.discover(start_dir=os.getcwd() + tmp + 'Cases', pattern='B_Get_filelist.py')
    # suite = unittest.defaultTestLoader.discover(start_dir=os.getcwd() + tmp + 'Cases', pattern='C_Search_file.py')
    # suite = unittest.defaultTestLoader.discover(start_dir=os.getcwd() + tmp + 'Cases', pattern='D_Open_file.py')
    # suite = unittest.defaultTestLoader.discover(start_dir=os.getcwd() + tmp + 'Cases', pattern='E_Rename_file.py')
    # suite = unittest.defaultTestLoader.discover(start_dir=os.getcwd() + tmp + 'Cases', pattern='F_Save_file.py')
    # suite = unittest.defaultTestLoader.discover(start_dir=os.getcwd() + tmp + 'Cases', pattern='G_Delete_file.py')
    # suite2 = unittest.defaultTestLoader.discover(start_dir=os.getcwd() + tmp + 'Cases', pattern='F_Save_file.py')
    # suite.addTests(suite2)
    # HTMLTestReportCN.HTMLTestRunner(stream=open(os.getcwd() + tmp + 'Output' + tmp + 'report.html', 'wb'),
    #                                 title='Wood接口自动化测试报告', description=Parametrized.ParametrizedTestCase.env+"环境测试报告",
    #                                 tester='Bo_lin Chen').run(suite)

    # 方式3：通过正则指定所有接口
    suite = unittest.defaultTestLoader.discover(start_dir=os.getcwd() + tmp + 'Cases', pattern='*.py')
    HTMLTestReportCN.HTMLTestRunner(stream=open(os.getcwd() + tmp + 'Output' + tmp + 'report.html', 'wb'),
                                    title='Wood接口自动化测试报告', description=Parametrized.ParametrizedTestCase.env+"环境测试报告",
                                    tester='Bo_lin Chen').run(suite)
    # print(suite)
