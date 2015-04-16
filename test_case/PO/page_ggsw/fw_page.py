# -*- coding: UTF-8 -*-
import time
from test_case.PO import BasePage
class fw_page(BasePage.Action):
    def main_menu_fwlbwh(self):
        '''公共事务--发文--发文类别维护'''
        self.select_main_menu(u'公共事务', u'发文', u'发文类别维护')
        self.iframe('iframe')
        
    def main_menu_fwgl(self):
        '''公共事务--发文--发文管理'''
        self.select_main_menu(u'公共事务', u'发文', u'发文管理')
        self.iframe('iframe')
        
    def main_menu_fwll(self):
        '''公共事务--发文--发文浏览'''
        self.select_main_menu(u'公共事务', u'发文', u'发文浏览')
        self.iframe('iframe')
        
    def main_menu_hg(self):
        '''公共事务--发文--核稿'''
        self.select_main_menu(u'公共事务', u'发文', u'核稿')
        self.iframe('iframe')
        
    def type_name(self,text):
        self.send_keys(u'发文类别名', text)
        
    def pxnum(self,text):
        self.send_keys(u'排序号', text)
        
    def select_add_type(self):
        self.click(u'新增-发文类别list:')
    
    def check_add_type(self):
        self.element_present(u'新增-发文类别list:')
        
    def select_type(self):
        self.click(u'发文类别list')
        
    def check_type(self):
        self.element_present(u'发文类别list')
        
    def check_type_no(self):
        self.element_no_present(u'发文类别list')
        
    def file_name(self,text):
        self.send_keys('文件名称', text)
        
    def file_num(self,text):
        self.send_keys('文件号', text)
        
    def Release_range(self):
        self.double_click(u'发布范围')
        
    def Examiner(self):
        self.double_click(u'核稿人')
        
    def select_user_all(self):
        self.click(u'选择公司')
        users = self.find_elements(u'选择人员all')
        for user in users:
            user.click()
            
    def select_user(self):
        self.click(u'选择公司')
        self.click(u'选择人员')
        
    def select_add_file(self):
        self.click(u'新增-文件名称list')
        
    def select_file(self):
        self.click(u'文件名称list')
    
    def double_file(self):
        self.double_click(u'文件名称list')
        
    def check_add_file(self):
        self.element_present(u'新增-文件名称list')
        
    def check_file(self):
        self.element_present(u'文件名称list')
        
    def check_file_no(self):
        self.element_no_present(u'文件名称list')
