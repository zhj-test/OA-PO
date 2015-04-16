# -*- coding: UTF-8 -*-
import unittest,time
from selenium import webdriver
from test_case.PO.page_xngl import YCYA_page
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
        time = time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time()+86400))
        self.YCYA = YCYA_page.YCYA_page(self.driver)
        self.public = public_page.public_page(self.driver)

        self.public.login('wangwh','111111')


    def test_fw(self):
        self.xdzl_xz1()
        self.xdzl_xz()
        self.xdzl_sc()
    
    def xdzl_xz1(self):
        print u'<---------------下达的指令1--------------->'
        self.YCYA.main_menu_xddzl()
        self.public.add()
        self.YCYA.finish_time(time)
        self.YCYA.receiver(u'管理员')
        self.YCYA.checker(u'王卫华')
        self.YCYA.inscontent(u'中午吃五个馒头')
        self.public.submit()
        self.YCYA.check_add_YCYA()
        
    def xdzl_xz(self):
        print u'<---------------下达的指令-新增--------------->'
        self.YCYA.main_menu_xddzl()
        self.public.add()
        self.YCYA.finish_time(time)
        self.YCYA.receiver(u'管理员')
        self.YCYA.checker(u'王卫华')
        self.YCYA.inscontent(u'明天提交测试总结报告')
        self.public.submit()
        self.YCYA.check_add_YCYA()
        
    def xdzl_sc(self):
        print u'<---------------下达的指令-删除--------------->'
        self.YCYA.main_menu_xddzl()
        self.YCYA.select_add_YCYA()
        self.public.delete()
        self.YCYA.check_add_YCYA_no()
        
    def 
        
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    unittest.main()