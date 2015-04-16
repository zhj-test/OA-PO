# -*- coding: UTF-8 -*-
import unittest,time
from selenium import webdriver
from test_case.PO.page_rlzy import pxjl_page
from test_case.PO import public_page

class case_pxjl(unittest.TestCase):
    def setUp(self):
        
        u'''
                初始化用例
                实例化Page类
                实现登录
        '''
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.starttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        self.endtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()+86400))
        
        self.pxjl = pxjl_page.pxjl_page(self.driver)
        self.public = public_page.public_page(self.driver)

        self.public.login('ycadmin','111111')
        
    def test_pxjl(self):
        #self.pxjl_xz()
        #self.pxjl_bj()
        self.pxjl_sc()
        self.public.quit()
    
    def pxjl_xz(self):
        print u'<---------------培训记录新增--------------->'
        self.pxjl.main_menu_pxjl()
        self.public.add()
        self.pxjl.StaffName(u'软件测试基础')
        self.pxjl.Company(u'济南东正科技')
        self.pxjl.SendRealName()
        self.public.ok()
        self.pxjl.start_time(self.starttime)
        self.pxjl.end_time(self.endtime)
        self.public.submit()
        self.pxjl.check_add_list()
        
    def pxjl_bj(self):
        print u'<---------------培训记录编辑--------------->'
        self.pxjl.main_menu_pxjl()
        self.pxjl.select_add_list()
        self.public.edit()
        self.pxjl.StaffName(u'软件自动化测试培训')
        self.public.submit()
        self.pxjl.check_list()
        
    def pxjl_sc(self):
        print u'<---------------培训记录删除--------------->'
        self.pxjl.main_menu_pxjl()
        self.pxjl.select_list()
        self.public.delete()
        self.pxjl.check_list_no()
        
if __name__ == "__main__":
    unittest.main()
        
        
    
    