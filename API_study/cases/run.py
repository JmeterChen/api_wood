import unittest
import HTMLTestRunnerCN
import sys

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(case01.Case01('test_case01'))
    # suite.addTest(case02.Case02('test_case02'))
    # suite.addTest(case03.Case03('test_case03'))
    # suite.addTest(case04.Case04('test_case04'))
    # unittest.TextTestRunner().run(suite)
    suite = unittest.defaultTestLoader.discover(start_dir=sys.argv[0]+'\\..\\', pattern='*.py')
    HTMLTestRunnerCN.HTMLTestRunner(stream=open(sys.argv[0]+'\\..\\report.html', 'wb')).run(suite)
    # unittest.TextTestRunner().run(suite)