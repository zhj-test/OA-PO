# -*- coding: UTF-8 -*-
#import time
from test_case.PO import BasePage
from selenium.webdriver.common.keys import Keys
class YCYA_page(BasePage.Action):
    def main_menu_xddzl(self):
        '''效能管理--YCYA指令--下达的指令'''
        self.select_main_menu(u'效能管理', u'YCYA指令', u'下达的指令')
        self.iframe('iframe')
        
    def main_menu_jcdzl(self):
        '''效能管理--YCYA指令--检查的指令'''
        self.select_main_menu(u'效能管理', u'YCYA指令', u'检查的指令')
        self.iframe('iframe')
        
    def main_menu_zxdzl(self):
        '''效能管理--YCYA指令--执行的指令'''
        self.select_main_menu(u'效能管理', u'YCYA指令', u'执行的指令')
        self.iframe('iframe')

    def main_menu_zlsz(self):
        '''效能管理--YCYA指令--YCYA指令设置'''
        self.select_main_menu(u'效能管理', u'YCYA指令', u'YCYA指令设置')
        self.iframe('iframe') 
        
    def finish_time(self,text):
        self.send_keys(u'完成时间', text)
        
    def receiver(self,text):
        self.send_keys(u'执行人', text)
        self.send_keys(u'奖惩人员', Keys.DOWN, False)
        self.send_keys(u'奖惩人员', Keys.ENTER)
        
    def checker(self,text):
        self.send_keys(u'检查人', text)
        self.send_keys(u'奖惩人员', Keys.DOWN, False)
        self.send_keys(u'奖惩人员', Keys.ENTER)
        
    def inscontent(self,text):
        self.send_keys(u'YCYA内容', text)
        
    def check_add_YCYA(self):
        self.element_present(u'下达命令新增列表list')
        
    def check_add_YCYA_no(self):
        self.element_no_present(u'下达命令新增列表list')
    
    def check_YCYA(self):
        self.element_present(u'下达命令新增列表list')
        
    def select_add_YCYA(self):
        self.click(u'下达命令新增列表list')
        
    def select_YCYA(self):
        self.click(u'下达命令列表list')