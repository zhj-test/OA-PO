# -*- coding: UTF-8 -*-
import unittest,time
from selenium import webdriver
from test_case.PO.page_xxjl import tp_page
from test_case.PO import public_page

class case_nbyj(unittest.TestCase):
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
        #self.file_path = 'E:\\script\\myselenium\\OA-PO\\data\\location_element.yaml'
    
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.starttime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        self.endtime = time.strftime("%Y-%m-%d",time.localtime(time.time()+86400))
        
        #BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        #self.file_path = os.path.join(BASE_DIR,"data","xxjl.yaml")
        #self.public_path = os.path.join(BASE_DIR,"data","public.yaml")
        
        self.tp = tp_page.tp_page(self.driver)
        self.public = public_page.public_page(self.driver)

        self.public.login('ycadmin','111111')
        
    def test_nbyj(self):
        self.tpgl_xz()
        self.tpgl_bj()
        self.tpgl_tpxm()
        self.tpgl_sx()
        self.tpll_tp()
        self.tpgl_sc()
        self.public.quit()
    
    def tpgl_xz(self):
        print u'<---------------投票管理-新增--------------->'
        self.tp.main_menu_tpgl()
        self.public.add()
        self.tp.Title(u'展开软件测试学习')
        self.tp.starttime(self.starttime)
        self.tp.endtime(self.endtime)
        self.tp.published_range()
        self.public.ok()
        self.public.submit()
        self.tp.check_add_list()
        
    def tpgl_bj(self):
        print u'<---------------投票管理-编辑--------------->'
        self.tp.main_menu_tpgl()
        self.tp.select_add_list()
        self.public.edit()
        self.tp.Title(u'组织春游投票')
        self.public.submit()
        self.tp.check_list()
        
    def tpgl_sc(self):
        print u'<---------------投票管理-删除--------------->'
        self.tp.main_menu_tpgl()
        self.tp.select_list()
        self.public.delete()
        self.tp.check_list_no() 
        
    def tpgl_tpxm(self):
        print u'<---------------投票管理-投票选择项--------------->'
        self.tp.main_menu_tpgl()
        self.tp.vote_item()
        for i in xrange(1,4):
            self.tp.option_add(i)
            self.tp.option(i)
            self.public.ok()
            self.driver.refresh()
            
    def tpgl_sx(self):
        print u'<---------------投票管理-立即生效--------------->'
        self.tp.main_menu_tpgl()        
        self.tp.into_force()
        self.driver.refresh()
    
    def tpll_tp(self):
        print u'<---------------投票管理-参加投票--------------->'
        self.tp.main_menu_tpll()
        self.tp.select_list()
        self.tp.vote()
        self.tp.select_vote_list()
        self.public.add()
        self.driver.refresh()

        
        
        
if __name__ == "__main__":
    unittest.main()