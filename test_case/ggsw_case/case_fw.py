# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from test_case.PO.page_ggsw import fw_page
from test_case.PO import public_page

class case_fw(unittest.TestCase):
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

        self.fw = fw_page.fw_page(self.driver)
        self.public = public_page.public_page(self.driver)

        self.public.login('ycadmin','111111')
        
        
    def test_fw(self):
        self.fwlbwh_xz()
        self.fwlbwh_bj()
        self.fwgl_xz()
        self.fwgl_bj()
        self.hg()
        self.fwgl_sc()
        self.fwlbwh_sc()
        
        
    def fwlbwh_xz(self):
        print u'<---------------发文类别维护-新增--------------->'
        self.fw.main_menu_fwlbwh()
        self.public.add()
        self.fw.type_name(u'内部通告-新增')
        self.fw.pxnum('9')
        self.public.submit()
        self.fw.check_add_type()

    def fwlbwh_bj(self):
        print u'<---------------发文类别维护-编辑--------------->'
        self.fw.main_menu_fwlbwh()
        self.fw.select_add_type()
        self.public.edit()
        self.fw.type_name(u'事务性通知')
        self.public.submit()
        self.fw.check_type()
        
    def fwgl_xz(self):
        print u'<---------------发文管理-新增--------------->'
        self.fw.main_menu_fwgl()
        self.fw.select_type()
        self.public.add()
        self.fw.file_name(u'2014公司一号文-新增')
        self.fw.pxnum('9')
        self.fw.file_num('304A')
        self.public.submit()
        self.fw.check_add_file()
        
    def fwgl_bj(self):
        print u'<---------------发文管理-编辑--------------->'
        self.fw.main_menu_fwgl()
        self.fw.select_type()
        self.fw.select_add_file()
        self.public.edit()
        self.fw.file_name(u'2015红头文件001')
        self.public.submit()
        self.fw.check_file()
        
    def hg(self):
        print u'<---------------核稿--------------->'
        self.fw.main_menu_hg()
        
        
        
    def fwll(self):
        print u'<---------------发文浏览--------------->'
        self.fw.main_menu_fwll()
        self.fw.select_type()
        
        
    def fwgl_sc(self):
        print u'<---------------发文管理-删除--------------->'
        self.fw.main_menu_fwlbwh()
        self.fw.select_type()
        self.fw.select_file()
        self.public.delete()
        
        self.fw.check_file_no()
        
    def fwlbwh_sc(self):
        print u'<---------------发文类别维护-删除--------------->'
        self.fw.main_menu_fwlbwh()
        self.fw.select_type()
        self.public.delete()
        self.fw.check_type_no()
   
        
if __name__ == "__main__":
    unittest.main()  