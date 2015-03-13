# -*- coding: UTF-8 -*-
from test_case.PO import BasePage

class ggl_page(BasePage.Action):
    def main_menu(self):
        self.select_main_menu(u'选择个人事务',u'选择公告栏', u'选择公告浏览')
        self.iframe('iframe')
        
    def notice_category_name(self,text):
        self.send_keys('公告类别名', text)
        
    #def notice_category_select(self):
    
    
    def a(self):
        self.double_click('公告栏管理员')
        
        
    