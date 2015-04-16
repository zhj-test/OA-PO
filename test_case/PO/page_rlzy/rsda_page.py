# -*- coding: UTF-8 -*-
import time
from test_case.PO import BasePage
#from selenium.webdriver.common.keys import Keys
class rsda_page(BasePage.Action):
    def main_menu_dagl(self):
        '''人力资源--人事档案--档案管理'''
        self.select_main_menu(u'人力资源', u'人事档案', u'档案管理')
        self.iframe('iframe')
        
    def main_menu_rsht(self):
        '''人力资源--人事档案--人事合同'''
        self.select_main_menu(u'人力资源', u'人事档案', u'人事合同')
        self.iframe('iframe')
        
    def RealName(self,text):
        self.send_keys(u"真实姓名", text)
        
    def WorkNum(self,text):
        self.send_keys(u"工号", text)
        
    def Unit(self):
        self.double_click(u'部门名称')
        self.switch_frame('frame_1')
        self.click(u'选择公司')
        self.click(u'选择部门')
    
    def Post(self):
        self.double_click(u'职位')
        self.switch_frame('frame_2')
        self.click(u'职位选择')
        
    def select_archives_add(self):
        self.click(u'档案新增list')
        
    def check_archives_add(self):
        self.element_present(u'档案新增list')
        
    def select_archives(self):
        self.click(u'档案list')
    
    def check_archives(self):
        self.element_present(u'档案list')
    
    def check_archives_no(self):
        self.element_no_present(u'档案list')
        
    def Contract_add(self):
        self.click(u'新建合同信息')
        self.switch_to_frame('khxx')
        time.sleep(2)
        
    def name(self):
        self.double_click(u'签约人员')
        self.switch_frame('frame_0')
        self.click(u'选择公司')
        self.click(u'选择人员')
        self.click(u'点击确定')
        self.iframe('iframe')
        self.switch_to_frame('khxx')
        
    def Contract_num(self,text):
        self.send_keys(u'合同编号', text)
        
    def Deadline(self,text):
        self.send_keys(u'满约日期', text)
    
    def check_contract_add(self):
        self.element_present(u'合同新增list')
    
    def check_contract(self):
        self.element_present(u'合同list')
        
    def check_contract_no(self):
        self.element_no_present(u'合同list')
        
    def edit_contract(self):
        self.click(u'合同编辑')
        self.switch_frame('frame_0')
        
    def delect_contract(self):
        self.click(u'合同删除')
        time.sleep(1)
        self.click(u'确定删除')
        self.iframe('iframe')
        time.sleep(1)
        
    
        