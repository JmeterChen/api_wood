# coding:utf-8
import unittest
import HTMLTestRunnerCN
import sys

import case01,case02,case03,case04


if __name__ == '__main__':

	# # 方案一：一个用例一个用例添加到指定测试集合后一起执行！
	# suite = unittest.TestSuite()                # 新建一个变量，等会来存放需要自动化的测试用例
	# suite.addTest(case01.Case01('test_case01')) # 将case01包中的用例test_case01加进suite对象
	# suite.addTest(case01.Case01('test_case02')) # 将case01包中的用例test_case02加进suite对象
	# suite.addTest(case02.Case02('test_case02')) # 将case02包中的用例test_case02加进suite对象 
	# suite.addTest(case03.Case03('test_case03'))
	# suite.addTest(case04.Case04('test_case04'))
	# # 注意上述将用例添加到suite对象中是不可以一次添加多个的，只能一个一个的添加！！！
	# unittest.TextTestRunner().run(suite)

	# # 方案二：通过正则去寻找符合条件的case文件，然后执行该文件包中的用例！
	suite = unittest.defaultTestLoader.discover(start_dir='./', pattern='case*.py')
	# unittest.TextTestRunner().run(suite)

	# 方案三：测试用例设计思路 一个接口  一个py文件 一个类  对应N个测试用例

	suite = unittest.defaultTestLoader.discover(start_dir=sys.argv[0]+'\\..\\', pattern='*.py')
	HTMLTestRunnerCN.HTMLTestRunner(stream=open(sys.argv[0]+'\\..\\report.html', 'wb')).run(suite)
	# unittest.TextTestRunner().run(suite)
