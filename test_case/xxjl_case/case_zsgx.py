# -*- coding: UTF-8 -*-
import unittest,time,os
from selenium import webdriver
from test_case.PO.page_xxjl import zsgx_page
from test_case.PO import public_page

class case_pxjl(unittest.TestCase):
    def setUp(self):
        
        u'''
                初始化用例
                实例化Page类
                实现登录
        '''
        '''
        chromedriver ="D:\ProgramFiles\chrome\Chrome-bin\chromedriver.exe"

        os.environ["webdriver.chrome.driver"] = chromedriver

        self.driver = webdriver.Chrome(chromedriver)
        '''
        self.driver = webdriver.Firefox()
    
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        #self.starttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        #self.endtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()+86400))
        
        self.zsgx = zsgx_page.zsgx_page(self.driver)
        self.public = public_page.public_page(self.driver)

        self.public.login('ycadmin','111111')
        
    def test_zsgx(self):
        #self.wjj_xz()
        #self.wjj_bj()
        #self.wj_xz()
        #self.wj_bj()
        #self.wj_ll()
        #self.wj_sc()
        self.wjj_sc()
        self.public.quit()
    
    def wjj_xz(self):
        print u'<---------------知识共享平台管理-文件夹-新增--------------->'
        self.zsgx.main_menu_zsgxgl()
        self.zsgx.file_add()
        self.zsgx.file_name(u'软件测试')
        self.zsgx.file_PxNum('9')
        self.zsgx.GxUnitName()
        self.public.ok()
        self.public.submit()
        self.zsgx.check_add_file()
        
    def wjj_bj(self):
        print u'<---------------知识共享平台管理-文件夹-编辑--------------->'
        self.zsgx.main_menu_zsgxgl()
        self.zsgx.select_add_file()
        self.zsgx.file_edit()
        self.zsgx.file_name(u'自动化测试')
        self.public.submit()
        self.zsgx.check_file()
        
    def wjj_sc(self):
        print u'<---------------知识共享平台管理-文件夹-删除--------------->'
        self.zsgx.main_menu_zsgxgl()        
        self.zsgx.select_file()
        self.zsgx.file_del()
        self.zsgx.check_file_no()
        
    def wj_xz(self):
        print u'<---------------知识共享平台管理-文件-新增--------------->'
        self.zsgx.main_menu_zsgxgl()
        self.zsgx.select_file()
        self.public.add()
        self.zsgx.Page_Name('QTP')
        self.zsgx.page_pxnum('9')
        self.zsgx.Upload()
        self.public.Upload()
        self.public.submit()
        self.zsgx.check_add_page()
        
    def wj_bj(self):
        print u'<---------------知识共享平台管理-文件-编辑--------------->'
        self.zsgx.main_menu_zsgxgl()
        time.sleep(2)
        self.zsgx.select_file()
        time.sleep(3)
        self.zsgx.select_add_page()
        time.sleep(2)
        self.public.edit()
        print '111111111111111'
        time.sleep(2)
        self.zsgx.Page_Name('selenium')
        self.public.submit()
        self.zsgx.check_page()
        
    def wj_sc(self):
        print u'<---------------知识共享平台管理-文件-删除--------------->'
        self.zsgx.main_menu_zsgxgl()
        self.zsgx.select_file()
        self.zsgx.select_page()
        self.public.delete()
        self.zsgx.check_page_no()
        
    def wj_ll(self):
        print u'<---------------知识共享平台浏览--------------->'
        self.zsgx.main_menu_zsgxll()
        self.zsgx.select_file()
        self.zsgx.Browse_page()
        self.zsgx.check_pagename('selenium')
    
    
        


if __name__ == "__main__":
    unittest.main()