# coding:utf-8
import unittest
import HTMLTestRunnerCN
import sys,time
import A_Login, B_Get_filelist, C_Search_file, D_Open_file
import E_Rename_file, F_Save_file, G_Delete_file, H_Logout
 
 
if __name__ == '__main__':

    # 方式1：控制单条用例执行
    suite = unittest.TestSuite()
    # suite.addTest(A_Login.Login('test_01_wood_login01'))
    # suite.addTest(A_Login.Login('test_02_wood_login02'))
    # suite.addTest(A_Login.Login('test_03_wood_login03'))
    # suite.addTest(B_Get_filelist.Get_filelist('test_04_get_filelist01'))
    # suite.addTest(B_Get_filelist.Get_filelist('test_05_get_filelist02'))
    # suite.addTest(C_Search_file.Search_file('test_06_search_file01'))
    # suite.addTest(C_Search_file.Search_file('test_07_search_file02'))
    # suite.addTest(D_Open_file.Open_file('test_08_open_file01'))
    # suite.addTest(D_Open_file.Open_file('test_09_open_file02'))
    # suite.addTest(D_Open_file.Open_file('test_10_open_file03'))
    # suite.addTest(D_Open_file.Open_file('test_11_open_file04'))
    # suite.addTest(D_Open_file.Open_file('test_12_open_file05'))
    # suite.addTest(E_Rename_file.Rename_file('test_13_rename_file01'))
    # suite.addTest(E_Rename_file.Rename_file('test_14_rename_file02'))
    # suite.addTest(E_Rename_file.Rename_file('test_15_rename_file03'))
    # suite.addTest(F_Save_file.Save_file('test_15_save01'))
    # suite.addTest(F_Save_file.Save_file('test_16_save02'))
    # suite.addTest(F_Save_file.Save_file('test_17_save03'))
    # suite.addTest(F_Save_file.Save_file('test_18_save04'))
    # suite.addTest(F_Save_file.Save_file('test_19_save05'))
    # suite.addTest(F_Save_file.Save_file('test_20_save06'))
    # suite.addTest(G_Delete_file.Delete_file('test_21_delete_file01'))
    # suite.addTest(G_Delete_file.Delete_file('test_22_delete_file02'))
    # suite.addTest(G_Delete_file.Delete_file('test_23_delete_file03'))
    # suite.addTest(G_Delete_file.Delete_file('test_24_delete_file04'))
    # suite.addTest(G_Delete_file.Delete_file('test_25_delete_file05'))
    # suite.addTest(H_Logout.Logout('test_26_logout'))
    # suite.addTest(H_Logout.Logout('test_27_logout'))

    # unittest.TextTestRunner().run(suite)
    suite = unittest.defaultTestLoader.discover(start_dir=sys.argv[0]+'\..\\', pattern='*.py')
    HTMLTestRunnerCN.HTMLTestRunner(stream=open(sys.argv[0]+'\\..\\Output_case\\report.html', 'wb'), title='Wood_API', description='WoodAPI_demo' ,tester='ChenBolin').run(suite)

    # 方式2 通过正则寻找用例文件一起执行
    # suite = unittest.TestSuite()
    # suite = unittest.defaultTestLoader.discover(start_dir=sys.argv[0]+'\\..\\', pattern='*.py')
    # HTMLTestRunnerCN.HTMLTestRunner(stream=open(sys.argv[0]+'\\..\\Output_all\\report.html', 'wb'), title='Wood_apiAutoTest', description='WoodAPI_demo' ,tester='ChenBolin').run(suite)
    # unittest.TextTestRunner().run(suite)