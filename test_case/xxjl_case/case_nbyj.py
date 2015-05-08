# -*- coding: UTF-8 -*-
import unittest,os
from selenium import webdriver
from test_case.PO.page_xxjl import nbyj_page
from test_case.PO import public_page

class case_nbyj(unittest.TestCase):
    def setUp(self):
        
        u'''
                初始化用例
                实例化Page类
                实现登录
        '''
        chromedriver ="D:\ProgramFiles\chrome\Chrome-bin\chromedriver.exe"

        os.environ["webdriver.chrome.driver"] = chromedriver

        self.driver = webdriver.Chrome(chromedriver)
        
        #self.driver = webdriver.Firefox()
        #self.file_path = 'E:\\script\\myselenium\\OA-PO\\data\\location_element.yaml'
    
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        #self.starttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        #self.endtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()+86400))
        
        #BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        #self.file_path = os.path.join(BASE_DIR,"data","xxjl.yaml")
        #self.public_path = os.path.join(BASE_DIR,"data","public.yaml")
        
        self.nbyj = nbyj_page.nbyj_page(self.driver)
        self.public = public_page.public_page(self.driver)

        
        
    def test_nbyj(self):
        #self.xx()
        #self.hf()
        self.sc()
        self.public.quit()
        
    def xx(self):
        print u'<---------------写信--------------->'
        self.public.login('ycadmin','111111')
        self.nbyj.main_menu_tlqlb()
        self.nbyj.WriteBtn()
        self.nbyj.Addressee(u'朱栋林')
        self.nbyj.ueditor(u'111111qqqqqq!@#$%^&*哈哈')
        self.nbyj.title(u'软件测试启动')
        self.public.submit()
        self.nbyj.sent()
        self.nbyj.check_list()  
        
        
        
    def hf(self):
        print u'<---------------回复--------------->'
        self.public.login('zhudl','111111')
        self.nbyj.main_menu_tlqlb()
        self.nbyj.double_list()
        self.nbyj.Reply()
        self.public.ueditor(u'111111qqqqqq!@#$%^&*哈哈')
        self.driver.switch_to_frame('Liframe')
        self.public.submit()
        
    def sc(self):
        print u'<---------------删除--------------->'
        self.public.login('ycadmin','111111')
        self.nbyj.main_menu_tlqlb()
        self.nbyj.sent()
        self.nbyj.select_list()
        self.public.delete()
        self.nbyj.check_list_no()
          
        
if __name__ == "__main__":
    unittest.main()