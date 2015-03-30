# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from test_case.PO.page_xngl import gzfx_page
from test_case.PO import public_page

class case_gzfx(unittest.TestCase):
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

        self.gzfx = gzfx_page.gzfx_page(self.driver)
        self.public = public_page.public_page(self.driver)

        self.public.login('ycadmin','111111')
        
    def test_gzfx(self):
        self.fxqsz_xz()
        self.fxqsz_bj()
        self.gzrsz()
        self.gzfx_xz()
        self.gzfx_bj()
        self.fxqsz_sc()
        self.gzfx_sc()
    
    def fxqsz_xz(self):
        print u'<---------------分享区设置-新增--------------->'
        self.gzfx.main_menu_fxqsz()
        self.public.add()
        self.gzfx.ShareArea(u'小笑话-新增')
        self.public.submit()
        
    def fxqsz_bj(self):
        print u'<---------------分享区设置-编辑--------------->'
        self.gzfx.main_menu_fxqsz()
        self.gzfx.select_add_ShareArea()
        self.public.edit()
        self.gzfx.ShareArea(u'小笑话-新增')
        self.public.submit()
    
    def gzrsz(self):
        print u'<---------------关注人设置-编辑--------------->'
        self.gzfx.main_menu_gzrsz()
        self.gzfx.select_company()
        users = self.gzfx.select_user()
        for user in users:
            user.click()
        self.gzfx.Unselect_all()
        self.gzfx.select_all()   
        self.public.submit() 
        
    def gzfx_xz(self):
        print u'<---------------工作分享-新增--------------->'
        self.gzfx.main_menu_gzfx()
        self.gzfx.tab_wfbd()
        self.public.add()
        self.gzfx.ShareTheme(u'逗你玩--新增')
        self.gzfx.Share_Area()
        self.public.submit()

    def gzfx_bj(self):
        print u'<---------------工作分享-编辑--------------->'
        self.gzfx.main_menu_gzfx()
        self.gzfx.tab_wfbd()
        self.gzfx.select_add_jobshare()
        self.public.edit()
        self.gzfx.ShareTheme(u'买赔了')
        self.gzfx.share_content('''坐电梯的时候听两个女生讲：“我刚去给电脑装了个内存条。”“多少钱啊？”“一百多。”“多大的呀？”“2G。”“唉你这样不划算，你还不如去网上买个移动硬盘呢，几十个G才一百多。”“啊，是吗？”听得我一愣一愣的。。''')
        self.public.submit()    
    
   
    def fxqsz_sc(self):
        print u'<---------------分享区设置-删除--------------->'
        self.gzfx.main_menu_fxqsz()
        self.gzfx.select_ShareArea()
        self.public.delete()
        self.driver.refresh()
        
    def gzfx_sc(self):
        print u'<---------------工作分享-删除--------------->'
        self.gzfx.main_menu_gzfx()
        self.gzfx.tab_wfbd()
        self.gzfx.select_jobshare()
        self.public.delete()
       
if __name__ == "__main__":
    unittest.main()