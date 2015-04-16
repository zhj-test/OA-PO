# -*- coding: UTF-8 -*-
import time
from test_case.PO import BasePage
#from selenium.webdriver.common.keys import Keys
class zsgx_page(BasePage.Action):
    def main_menu_zsgxgl(self):
        '''信息交流--知识共享--知识共享平台管理'''
        self.select_main_menu(u'信息交流', u'知识共享', u'知识共享平台管理')
        self.iframe('iframe')
        #time.sleep(2)
        
    def main_menu_zsgxll(self):
        '''信息交流--知识共享--知识共享平台管理'''
        self.select_main_menu(u'信息交流', u'知识共享', u'知识共享平台浏览')
        self.iframe('iframe')
        
    def file_name(self,text):
        self.send_keys(u'文件夹名称', text)
        
    def file_PxNum(self,text):
        self.send_keys(u'文件夹排序号', text)
        
    def GxUnitName(self):
        self.double_click(u'共享部门')
        self.switch_frame('frame_1')
        self.click(u'选择公司')
        self.click(u'选择部门')
        
    def file_add(self):
        self.click(u'新增文件夹')
        self.switch_frame('frame_0')
        
    def file_edit(self):
        self.click(u'编辑文件夹')
        self.switch_frame('frame_0')
        
    def file_del(self):
        self.click(u'删除文件夹')
        time.sleep(1)
        self.click(u'确定删除')
        self.iframe('iframe')
        time.sleep(1)
        
    def select_add_file(self):
        self.click(u'文件列表新增list')
    
    def select_file(self):
        self.click(u'文件列表list')
        
    def check_add_file(self):
        self.element_present(u'文件列表新增list')
        
    def check_file(self):
        self.element_present(u'文件列表list')
        
    def check_file_no(self):
        self.element_no_present(u'文件列表list')
        
    def Page_Name(self,text):
        self.send_keys(u'文件名称', text)
        
    def page_pxnum(self,text):
        self.send_keys(u'文件排序号', text)
        
    def Upload(self):
        self.click(u'添加文件附件')
        
    def select_add_page(self):
        self.click(u'文件新增list')
        
    def select_page(self):
        self.click(u'文件list')
        
    def check_add_page(self):
        self.element_present(u'文件新增list')
        
    def check_page(self):
        self.element_present(u'文件list')
        
    def check_page_no(self):
        self.element_no_present(u'文件list')
             
    def Browse_page(self):
        self.double_click(u'文件list')
        self.switch_frame('frame_0')
        
    def check_pagename(self,text):
        assert self.text(u'文件名称'),text
        self.driver.refresh()
        
    
    
        
