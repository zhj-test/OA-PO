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
        
    def test_case(self):
        self.ggl_ggll()
        self.ggl_gglbbj()
        
        self.ggl_gglbsc()
        self.public.quit()
        
    def ggl_gglbxz(self):
        u'''公告栏类别新增'''
        print '----------公告栏类别新增用例开始----------'
        self.ggl.main_menu()
        self.ggl.add()
        #self.public.add()
        self.ggl.name(u'新增--假期类公告')
        self.ggl.FuzerenName()
        self.ggl.Fuzerenuser()
        self.ggl.Faburen()
        self.ggl.Fabuuser()
        self.public.submit()
        self.ggl.check_list()
        
    def ggl_gglbbj(self):
        pass
 
    def ggl_gglbsc(self):
        pass        
        
            
        
        
if __name__ == "__main__":
    unittest.main()
        
        