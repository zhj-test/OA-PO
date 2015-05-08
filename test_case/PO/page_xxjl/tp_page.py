# -*- coding: UTF-8 -*-
import time
from test_case.PO import BasePage
#from selenium.webdriver.common.keys import Keys
class tp_page(BasePage.Action):
    def main_menu_tpgl(self):
        '''信息交流--投票--投票管理'''
        self.select_main_menu(u'信息交流', u'投票', u'投票管理')
        self.iframe('iframe')
        
    def main_menu_tpll(self):
        '''信息交流--投票--投票浏览'''
        self.select_main_menu(u'信息交流', u'投票', u'投票浏览')
        self.iframe('iframe')
        
    def Title(self,text):
        self.send_keys(u'投票主题', text)
        
    def starttime(self,text):
        self.send_keys(u'投票开始时间', text)
        
    def endtime(self,text):
        self.send_keys(u'投票结束时间', text)
        
    def published_range(self):
        self.double_click(u'发布范围(部门)')
        self.switch_frame('frame_1')
        self.click(u'选择公司')
        self.click(u'选择部门')
        
    def select_add_list(self):
        self.click(u'主题新增列表list')
        
    def select_list(self):
        self.click(u'主题列表list')
        
    def check_add_list(self):
        self.element_present(u'主题新增列表list')
        
    def check_list(self):
        self.element_present(u'主题列表list')
        
    def check_list_no(self):
        self.element_no_present(u'主题列表list')
        
    def into_force(self):
        self.click(u'立即生效')
        time.sleep(1)
        self.click(u'确定删除')
        self.iframe('iframe')
        time.sleep(1)
        
    def vote_item(self):
        self.click(u'投票项目')
        self.switch_frame('frame_0')
        
    def vote(self):
        self.click(u'参加投票')
        self.switch_frame('frame_0')
        
    def option(self,text):
        self.send_keys(u'选项', text)
        
    def option_add(self,i):
        self.click(u'新增选项')
        frame = 'frame_'+'%s' % i
        self.switch_frame(frame)
        
    def option_edit(self):
        self.click(u'编辑选项')
        
    def option_del(self):
        self.click(u'删除选项')
        
    def select_vote_list(self):
        self.click(u'投票列表list')