# -*- coding: UTF-8 -*-
import unittest,time
from selenium import webdriver
from test_case.PO.page_xngl import ppf_page
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

        self.ppf = ppf_page.ppf_page(self.driver)
        self.public = public_page.public_page(self.driver)

        self.public.login('ycadmin','111111')
        
        
    def test_fw(self):
        self.ppfsq_xz()
        self.ppfsq_xz_1()
        self.ppfsq_cx()
        self.ppfsh()
        #self.ppfck()
        self.public.quit()
    
    def ppfsq_xz(self):
        self.ppf.main_menu_ppfsq()
        self.public.add()
        self.ppf.employee(u'管理员')
        self.ppf.brandscrocevalue('9')
        self.ppf.brandscore_reason(u'扶老太太过马路')
        self.public.submit()
        self.ppf.check_add_Fraction()
        
    def ppfsq_xz_1(self):
        self.ppf.main_menu_ppfsq()
        self.public.add()
        self.ppf.employee(u'管理员')
        self.ppf.brandscrocevalue('9')
        self.ppf.brandscore_reason(u'提前完成工作')
        self.public.submit()
        self.ppf.check_Fraction()
        
    def ppfsq_cx(self):
        self.ppf.main_menu_ppfsq()
        self.ppf.select_add_Fraction()
        self.public.delete()
        self.ppf.check_add_Fraction_no()
        
    def ppfsh(self):
        self.public.login('wangwh','111111')
        self.ppf.main_menu_ppfsh()
        self.ppf.select_pending_review()
        self.public.submit()
        
    def ppfck(self):
        #self.public.login('wangwh','111111')
        self.ppf.main_menu_ppfck()
        assert u'通过' == self.ppf.Check_out()
        
        
        
        
        
        
if __name__ == "__main__":
    unittest.main()  