# -*- coding: UTF-8 -*-
import time
import unittest
from selenium import webdriver
from test_case.PO import login_page
from test_case.PO import public_page
from test_case.PO.page_grsw import ggl_page
class ggl(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        
        #self.login = login_page.login_page(self.driver)
        self.ggl = ggl_page.ggl_page(self.driver)
        self.public = public_page.public_page(self.driver)

        self.public.login('ycadmin','111111')
        
    def test_ggl_ggll(self):
        self.ggl.main_menu()
        self.public.add()
        self.ggl.notice_category_name(text)
        self.ggl.
        
        
        
        
if __name__ == "__main__":
    unittest.main()
        
        