# -*- coding: UTF-8 -*-
#import time
import unittest
from selenium import webdriver
from test_case.PO import public_page
from test_case.PO.page_grsw import ggl_page
class ggl(unittest.TestCase):
    u'''公告栏'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

        self.ggl = ggl_page.ggl_page(self.driver)
        self.public = public_page.public_page(self.driver)

        self.public.login('ycadmin','111111')
        
    def test_ggl_ggll(self):
        u'''新增公告栏类别'''
        print '----------新增公告栏类别用用例开始----------'
        self.ggl.main_menu()
        self.public.add()
        self.ggl.notice_category_name(u'新增--假期类公告')
        self.ggl.FuzerenName()
        self.ggl.Fuzerenuser()
        self.ggl.Faburen()
        self.ggl.Fabuuser()
        self.public.submit()
        if self.ggl.category_add_list():
            print u'新增公告类别成功'
        else:
            print u'新增公告类别失败'
        
        
            
        self.public.quit()
        
if __name__ == "__main__":
    unittest.main()
        
        