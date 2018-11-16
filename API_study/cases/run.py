# coding:utf-8
import unittest
import Register, AddEvent, EventDetail   # 匹配方案1使用
import util
import HTMLTestRunnerCN


if __name__ == '__main__':

	# # 方案1：把要执行的用例放到一个测试套件里，一起执行
	# suite = unittest.TestSuite()
	# suite.addTest(Register.Register('test_register01'))
	# suite.addTest(Register.Register('test_register02'))
	# suite.addTest(AddEvent.AddEvent('test_add_event01'))
	# suite.addTest(EventDetail.EventDetail('test_get_eventdetail01'))
	# unittest.TextTestRunner().run(suite)

	# 方案2：通过正则去匹配要执行的用例文件
	suite = unittest.defaultTestLoader.discover(start_dir='./',pattern='*.py')
	HTMLTestRunnerCN.HTMLTestRunner(stream=open('./report.html','wb')).run(suite)
	# unittest.TextTestRunner().run(suite)