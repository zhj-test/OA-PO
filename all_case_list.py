#coding=utf-8
#把 test_case 目录添加到 path 下，这里用的相对路径
import sys
sys.path.append("\test_case")
from test_case.ggsw_case import *
from test_case.grsw_case import *
#用例文件列表
def caselist():
    alltestnames = [case_clgl.case_clgl,case_xwgl.xwgl]
    return alltestnames