# -*- coding: UTF-8 -*-
import time
from test_case.PO import BasePage
#from selenium.webdriver.common.keys import Keys
class nbtl_page(BasePage.Action):
    def main_menu_tlqlb(self):
        '''信息交流--内部讨论--讨论区类别'''
        self.select_main_menu(u'信息交流', u'内部讨论', u'讨论区类别')
        self.iframe('iframe')
        #time.sleep(2)
        
    def main_menu_tlq(self):
        '''信息交流--内部讨论--讨论区'''
        self.select_main_menu(u'信息交流', u'内部讨论', u'讨论区')
        self.iframe('iframe')

    def Category_name(self,text):
        self.send_keys(u'讨论区类别名称', text)
        
    def Gkrealname(self):
        self.double_click(u'讨论区管理员')
        self.switch_frame('frame_1')
        self.click(u'选择公司')
        self.click(u'选择人员')
    
    def UnitName(self):
        self.double_click(u'公开部门')
        self.switch_frame('frame_2')
        self.click(u'选择公司')
        self.click(u'选择部门')
        
    def select_add_category_list(self):
        self.click(u'讨论区类别新增列表list')
        
    def select_category_list(self):
        self.click(u'讨论区类别列表list')
        
    def check_add_category_list(self):
        self.element_present(u'讨论区类别新增列表list')
        
    def check_category_list(self):
        self.element_present(u'讨论区类别列表list')
        
    def check_category_list_no(self):
        self.element_no_present(u'讨论区类别列表list')
        
    def double_category_list(self):
        self.double_click(u'讨论区类别列表list')
        self.switch_frame('frame_0')
        
    def discuss_theme(self,text):
        self.switch_frame('frame_1')
        self.send_keys(u'讨论主题', text)
        
    def select_theme_list(self):
        self.double_click(u'讨论区新增列表list')
        self.switch_frame('frame_1')
        
    def check_theme_list(self):
        self.switch_frame('frame_0')
        self.element_present(u'讨论区新增列表list')
        
    def reply_click(self):
        self.click(u'讨论区回复')
        
    def edit_click(self):
        self.click(u'讨论区修改')
        self.switch_frame('frame_2')
        
    def del_click(self):
        self.click(u'讨论区删除')
        time.sleep(1)
        self.click(u'确定删除')

        
        
    