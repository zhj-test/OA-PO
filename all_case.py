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

B_DIR = os.path.dirname(__file__)
path = os.path.join(B_DIR,'report',day_now)

if not os.path.exists(path):
    os.mkdir(path)
    
filename = os.path.join(path,'result'+ time_now+ '.html')

fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'OA自动化测试' ,description=u'用例执行情况： ')
#执行测试套件
runner.run(testunit)
