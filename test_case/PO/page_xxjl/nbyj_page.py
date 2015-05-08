# -*- coding: UTF-8 -*-
import time
from test_case.PO import BasePage
from selenium.webdriver.common.keys import Keys
class nbyj_page(BasePage.Action):
    def main_menu_tlqlb(self):
        '''信息交流--内部邮件--内部邮件'''
        self.select_main_menu(u'信息交流', u'内部邮件1', u'内部邮件2')
        self.iframe('iframe')
        
    def ueditor(self,text,ueditor='ueditor_0'):
        self.driver.switch_to_frame(ueditor) 
        self.send_keys(u'富文本框',text)
        time.sleep(1)

    def WriteBtn(self):
        self.click(u'写信')
        self.switch_to_frame('Liframe')
        
    def Addressee(self,text):
        self.send_keys(u'收件人', text)
        time.sleep(1)
        self.send_keys(u'收件人', Keys.ENTER)
        
    def title(self,text):
        self.iframe('iframe')
        self.switch_to_frame('Liframe')
        self.send_keys(u'邮件主题', text)
        
    def double_list(self):
        self.switch_to_frame('Liframe')
        self.double_click(u'邮件列表list')
        
    def select_list(self):
        self.switch_to_frame('Liframe')
        self.click(u'邮件列表list')
        
    def check_list(self):
        self.switch_to_frame('Liframe')
        self.element_present(u'邮件列表list')
        
    def check_list_no(self):
        self.switch_to_frame('Liframe')
        self.element_no_present(u'邮件列表list')
        
    def Reply(self):
        self.click(u'回复')
        
    def Inbox(self):
        self.click(u'收件箱')
        
    def draft_box(self):
        self.click(u'草稿箱')
        
    def sent(self):
        self.click(u'已发送')
        
    def was_deleted(self):
        self.iframe('iframe')
        self.click(u'已删除')
        self.switch_to_frame('Liframe')
        
    
        
        