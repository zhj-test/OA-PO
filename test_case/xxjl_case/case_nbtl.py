# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from test_case.PO.page_xxjl import nbtl_page
from test_case.PO import public_page

class case_pxjl(unittest.TestCase):
    def setUp(self):
        
        u'''
                初始化用例
                实例化Page类
                实现登录
        chromedriver ="D:\ProgramFiles\chrome\Chrome-bin\chromedriver.exe"

        os.environ["webdriver.chrome.driver"] = chromedriver

        self.driver = webdriver.Chrome(chromedriver)
        '''
        self.driver = webdriver.Firefox()
        self.file_path = 'E:\\script\\myselenium\\OA-PO\\data\\location_element.yaml'
    
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        #self.starttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        #self.endtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()+86400))
        
        #BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        #self.file_path = os.path.join(BASE_DIR,"data","xxjl.yaml")
        #self.public_path = os.path.join(BASE_DIR,"data","public.yaml")
        
        self.nbtl = nbtl_page.nbtl_page(self.driver)
        self.public = public_page.public_page(self.driver)

        self.public.login('ycadmin','111111')
        
    def test_nbtl(self):
        #self.tlqlb_xz()
        #self.tlqlb_bj()
        #self.tlq_ft()
        #self.tlq_hf()
        #self.tlq_xg()
        #self.tlq_sc()
        self.tlqlb_sc()
        self.public.quit()        
    
    def tlqlb_xz(self):
        print u'<---------------讨论区类别-新增--------------->'
        self.nbtl.main_menu_tlqlb()
        self.public.add()
        self.nbtl.Category_name(u'软件测试技术讨论')
        self.nbtl.Gkrealname()
        self.public.ok()
        self.nbtl.UnitName()
        self.public.ok()
        self.public.submit()
        self.nbtl.check_add_category_list()
        
    def tlqlb_bj(self):
        print u'<---------------讨论区类别-编辑--------------->'
        self.nbtl.main_menu_tlqlb()
        self.nbtl.select_add_category_list()
        self.public.edit()
        self.nbtl.Category_name(u'自动化技术讨论')
        self.public.submit()
        self.nbtl.check_category_list()
        
    def tlqlb_sc(self):
        print u'<---------------讨论区类别-删除--------------->'
        self.nbtl.main_menu_tlqlb()
        self.nbtl.select_category_list()
        self.public.delete()
        self.nbtl.check_category_list_no()
    
    def tlq_ft(self):
        print u'<---------------讨论区-发帖--------------->'
        self.nbtl.main_menu_tlq()
        self.nbtl.double_category_list()
        self.public.add()
        self.nbtl.discuss_theme(u'QTP与selenium')
        self.public.ueditor(u'!@#$%^&*QTPselenium讨论区-发帖1234567890')
        self.nbtl.discuss_theme(u'QTP与selenium')
        self.public.submit()
        self.nbtl.check_theme_list()
        
    def tlq_hf(self):
        print u'<---------------讨论区-回复--------------->'
        self.nbtl.main_menu_tlq()
        self.nbtl.double_category_list()
        self.nbtl.select_theme_list()
        self.public.ueditor(u'讨论区-回复内容')
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame('frame_1')
        self.public.submit()
        self.driver.refresh()
        
    def tlq_xg(self):
        print u'<---------------讨论区-修改--------------->'
        self.nbtl.main_menu_tlq()
        self.nbtl.double_category_list()
        self.nbtl.select_theme_list()
        self.nbtl.edit_click()
        self.public.ueditor(u'讨论区-回复内容修改 ')
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame('frame_2')
        self.public.submit()
        self.driver.refresh()
        
    def tlq_sc(self):
        print u'<---------------讨论区-删除--------------->'
        self.nbtl.main_menu_tlq()
        self.nbtl.double_category_list()
        self.nbtl.select_theme_list()  
        self.nbtl.del_click()
        self.driver.refresh()
        
        
        
        
        
        
        
if __name__ == "__main__":
    unittest.main()