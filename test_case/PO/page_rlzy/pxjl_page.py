# -*- coding: UTF-8 -*-
#import time
from test_case.PO import BasePage
#from selenium.webdriver.common.keys import Keys
class pxjl_page(BasePage.Action):
    def main_menu_pxjl(self):
        '''人力资源--培训记录--培训记录'''
        self.select_main_menu(u'人力资源', u'培训记录1', u'培训记录2')
        self.iframe('iframe')
        
    def StaffName(self,text):
        self.send_keys(u'培训项目', text)
        
    def Company(self,text):
        self.send_keys(u'培训单位', text)
        
    def SendRealName(self):
        self.double_click(u'参与用户')
        self.switch_frame('frame_1')
        self.click(u'选择公司')
        for use in self.find_elements(u'选择人员all'):
            use.click()
        
    def start_time(self,text):
        self.send_keys(u'开始时间', text)
        
    def end_time(self,text):
        self.send_keys(u'结束时间', text)
        
    def select_add_list(self):
        self.click(u'培训记录新增list')
        
    def select_list(self):
        self.click(u'培训记录list')
        
    def check_add_list(self):
        self.element_present(u'培训记录新增list')
        
    def check_list(self):
        self.element_present(u'培训记录list')
        
    def check_list_no(self):
        self.element_no_present(u'培训记录list')