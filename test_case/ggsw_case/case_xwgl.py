# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from test_case.PO import public_page
from test_case.PO.page_ggsw import xwgl_page
class xwgl(unittest.TestCase):
    u'''新闻管理模块测试用例'''
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

        self.xwgl = xwgl_page.xwgl_page(self.driver)
        self.public = public_page.public_page(self.driver)

        self.public.login('ycadmin','111111')
        
    def test_case(self):
        u'''新闻管理模块'''
        self.xwgl_xz()
        self.xwgl_bj()
        self.xwgl_fb()
        self.xwgl_ll()
        self.xwgl_qxfb()
        self.xwgl_sc()
        self.public.quit()
        
    def xwgl_xz(self):
        print u'<----------新闻新增用例开始---------->'
        self.xwgl.main_menu_xwgl()
        self.public.add()
        self.xwgl.title(u'新增--公司每日新闻第一条')#
        self.xwgl.GxUnitName()
        self.xwgl.GxUnituser()
        self.public.ueditor(u"1234567890\n!@#$%^&*()<>?.,\n\
大漠孤烟直，长河落日圆。\n abc def ghi")
        self.public.submit()
        
        if self.xwgl.category_add_list():
            self.driver.refresh()
        else:
            self.public.error_quit()
       
    def xwgl_bj(self):
        print u'<----------新闻编辑用例开始---------->'
        self.xwgl.main_menu_xwgl()
        self.xwgl.select_add_list()
        self.public.edit()
        self.xwgl.title(u'第一条新闻')
        self.public.submit()
        
        if self.xwgl.category_edit_list():
            self.driver.refresh()
        else:
            self.public.error_quit()

    def xwgl_fb(self):
        print u'<----------新闻发布用例开始---------->'
        self.xwgl.main_menu_xwgl()
        self.xwgl.select_edit_list()
        self.xwgl.release()
        self.driver.refresh()
        
    def xwgl_ll(self):
        print u'<----------新闻浏览用例开始---------->'
        self.xwgl.main_menu_xwll()
        self.xwgl.double_list()
        #print self.xwgl.title_text()
        #assert self.xwgl.title_text() == "第一条新闻"
        self.driver.refresh()
        
    def xwgl_qxfb(self):
        print u'<----------新闻取消发布用例开始---------->'
        self.xwgl.main_menu_xwgl()
        self.xwgl.select_edit_list()
        self.xwgl.cancel()
        
        self.driver.refresh()
        
    def xwgl_sc(self):
        print u'<----------新闻删除用例开始---------->'
        self.xwgl.main_menu_xwgl()
        self.xwgl.select_edit_list()
        self.public.delete()
        
        if self.xwgl.category_edit_list():
            self.public.error_quit()
        else:
            self.driver.refresh()
        
if __name__ == "__main__":
    unittest.main()
        