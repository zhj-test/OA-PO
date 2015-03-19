# -*- coding: UTF-8 -*
import os
import unittest
import HTMLTestRunner
import time
from test_case import *
import all_case_list

#创建测试套件
testunit=unittest.TestSuite()

cases = all_case_list.caselist()
for case in cases:
    testunit.addTest(unittest.makeSuite(case))
    
time_now = time.strftime("%H%M%S",time.localtime(time.time()))

day_now = time.strftime("%Y%m%d",time.localtime(time.time()))
#time_now = time.strftime("%H%M%S",time.localtime(time.time()))
if os.path.exists("E:\\script\\myselenium\\OA-PO\\report\\" + day_now):
    pass
else:
    os.mkdir("E:\\script\\myselenium\\OA-PO\\report\\" + day_now)
    
filename = "E:\\script\\myselenium\\OA-PO\\report\\"+ day_now+ '\\'+ 'result'+ time_now+ '.html'

#filename = "E:\\script\\myselenium\\OA-PO\\report\\"+ 'result_'+ time_now+ '.html'

fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'OA自动化测试' ,description=u'用例执行情况： ')
#执行测试套件
runner.run(testunit)


'''
#创建测试套件
testunit=unittest.TestSuite()

cases = all_case_list.caselist()
for case in cases:
    testunit.addTest(unittest.makeSuite(case))
time_now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filename = "E:\\script\\myselenium\\OA\\report\\"+ time_now+ 'result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'OA自动化测试' ,description=u'用例执行情况： ')
#执行测试套件
runner.run(testunit)
'''