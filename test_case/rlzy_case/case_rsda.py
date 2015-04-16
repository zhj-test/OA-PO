# -*- coding: UTF-8 -*-
import unittest,time
from selenium import webdriver
from test_case.PO.page_rlzy import rsda_page
from test_case.PO import public_page

class case_rsda(unittest.TestCase):
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
        self.Dtime = time.strftime("%Y-%m-%d",time.localtime(time.time()+86400))
        self.rsda = rsda_page.rsda_page(self.driver)
        self.public = public_page.public_page(self.driver)

        self.public.login('ycadmin','111111')


    def test_rsda(self):
        self.dagl_xz()
        self.dagl_bj()
        self.rsht_xz()
        self.rsht_bj()
        self.dagl_sc()
        self.rsht_sc()
        self.public.quit()
                
    def dagl_xz(self):
        print u'<---------------档案新增--------------->'
        self.rsda.main_menu_dagl()
        self.public.add()
        self.rsda.RealName(u'张三')
        self.rsda.WorkNum('fzg-xz-00001')
        self.rsda.Unit()
        self.public.ok()
        self.rsda.Post()
        self.public.ok()
        self.public.submit()
        self.rsda.check_archives_add()
        
    def dagl_bj(self):
        print u'<---------------档案编辑--------------->'
        self.rsda.main_menu_dagl()
        self.rsda.select_archives_add()
        self.public.edit()
        self.rsda.RealName(u'秦始皇')
        self.rsda.WorkNum('fzg-00001')
        self.public.submit()
        self.rsda.check_archives()
        
    def rsht_xz(self):
        print u'<---------------合同新增--------------->'
        self.rsda.main_menu_rsht()
        self.rsda.Contract_add()
        self.rsda.name()
        #self.public.ok()
        self.rsda.Contract_num('htbh-0001')
        self.rsda.Deadline(self.Dtime)
        self.public.submit()
        self.rsda.check_contract_add()
        
    def rsht_bj(self):
        print u'<---------------合同编辑--------------->'
        self.rsda.main_menu_rsht()
        self.rsda.edit_contract()
        self.rsda.Contract_num('htbh-0002')
        self.public.submit()
        self.rsda.check_contract()
        
    def rsht_sc(self):
        print u'<---------------合同删除--------------->'
        self.rsda.main_menu_rsht()
        self.rsda.delect_contract()
        self.rsda.check_contract_no()
        
    def dagl_sc(self):
        print u'<---------------档案删除--------------->'
        self.rsda.main_menu_dagl()
        self.rsda.select_archives()
        self.public.delete()
        self.rsda.check_archives_no()   
        
if __name__ == "__main__":
    unittest.main()