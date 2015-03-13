# -*- coding: UTF-8 -*-
import time
import unittest
from selenium import webdriver
from test_case.PO import login_page 
from test_case.public import *
class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        
        self.loginpage = login_page.login_page(self.driver)
        
    def test_login(self):
        self.loginpage.open_url()
        data = input_data.input_data(u'参数化用户')
        for account in data:
            print '-------------用例开始--------------' 
            print self.driver.title
            self.loginpage.TxtName(account[0])
            self.loginpage.TxtPwd(account[1])
            self.loginpage.login_button()
            
            if account[0]=='' or account[1]=='':
                aa = self.driver.switch_to_alert()
                alert_text =  aa.text
                try:
                    self.assertEqual(account[2], alert_text, '提示信息有误') # 断言value1 == value2   
                    time.sleep(1)
                    aa.accept() 
                except:
                    print u'运行失败！！！'
                    print account[:2] , u'实际显示提示信息:' , alert_text , u'&预测显示提示信息:', account[2]

            elif self.loginpage.errot_mtip():
                error_text = self.loginpage.errot_mtip().text
                try:
                    self.assertEqual(account[2], error_text, '提示信息有误') # 断言value1 == value2
                    print self.driver.title
                except:
                    print u'运行失败！！！'
                    print account[:2] , u'实际显示提示信息:' , error_text , u'&预测显示提示信息:', account[2]   
            
            else:    
                print u'登录成功'
            print '-------------用例结束--------------' 
            print ''
            time.sleep(3)
            
                
        
        
        
        
        
if __name__ == "__main__":
    unittest.main()
        
        