# -*- coding: UTF-8 -*-
from test_case.PO import BasePage

class ggl_page(BasePage.Action):
    
    def main_menu(self):
        self.select_main_menu(u'选择个人事务',u'选择公告栏', u'选择公告浏览')
        self.iframe('iframe')
        
    def notice_category_name(self,text):
        self.send_keys(u'公告类别名', text)
    
    def FuzerenName(self):
        self.double_click(u'公告栏管理员')
        self.switch_frame('frame_1')
        
    def Fuzerenuser(self):
        self.click(u'选择公司')
        self.click(u'选择人员')
        self.click(u'点击确定')
        self.switch_frame('frame_0')
        
    def Faburen(self):
        self.double_click(u'公告发布人')
        self.switch_frame('frame_2')
    
    def Fabuuser(self):
        self.click(u'选择公司')
        self.click(u'选择人员')
        self.click(u'点击确定')
        self.switch_frame('frame_0')
        
    def check_list(self):
        self.element_present(u'选择新增的公告类别')
        
    def category_add_list(self):
        return self.is_element_present(u'选择新增的公告类别')

    def category_list(self):
        return self.is_element_present(u'选择编辑后的公告类别')
