import unittest
import HTMLTestRunnerCN
import sys
# import Get_filelist
# import Search_file
# import Open_file
# import Rename_file
import Delete_file


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Delete_file.Delete_file('test_delete_file'))
    # suite.addTest(case02.Case02('test_case02'))
    # suite.addTest(case03.Case03('test_case03'))
    # suite.addTest(case04.Case04('test_case04'))
    # unittest.TextTestRunner().run(suite)
    # suite = unittest.defaultTestLoader.discover(start_dir=sys.argv[0]+'\\..\\', pattern='*.py')
    HTMLTestRunnerCN.HTMLTestRunner(stream=open(sys.argv[0]+'\\..\\report.html', 'wb')).run(suite)
    # unittest.TextTestRunner().run(suite)