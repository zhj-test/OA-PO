# -*- coding: UTF-8 -*-
import time
from test_case.PO import BasePage
from selenium.webdriver.common.keys import Keys
class ppf_page(BasePage.Action):
    def main_menu_ppfsq(self):
        '''效能管理--品牌分--品牌分申请'''
        self.select_main_menu(u'效能管理', u'品牌分', u'品牌分申请')
        self.iframe('iframe')
    
    def main_menu_ppfck(self):
        '''效能管理--品牌分--品牌分查看'''
        self.select_main_menu(u'效能管理', u'品牌分', u'品牌分查看')
        self.iframe('iframe')
        
    def main_menu_ppfsh(self):
        '''效能管理--品牌分--品牌分审核'''
        self.select_main_menu(u'效能管理', u'品牌分', u'品牌分审核')
        self.iframe('iframe')
    
    def main_menu_ppfphb(self):
        '''效能管理--品牌分--品牌分排行榜'''
        self.select_main_menu(u'效能管理', u'品牌分', u'品牌分排行榜')
        self.iframe('iframe')
        
    def employee(self,text):
        self.send_keys(u'奖惩人员', text)
        self.send_keys(u'奖惩人员', Keys.DOWN, False)
        self.send_keys(u'奖惩人员', Keys.ENTER)
        
    def brandscrocevalue(self,text):
        self.send_keys(u'奖惩分值', text)
        
    def brandscore_reason(self,text):
        self.send_keys(u'奖惩原因', text)
    
    def select_add_Fraction(self):
        self.click(u'品牌分申请-新增list')
        
    def select_Fraction(self):
        self.click(u'品牌分申请list')
        
    def check_add_Fraction(self):
        self.element_present(u'品牌分申请-新增list')
        
    def check_add_Fraction_no(self):
        self.element_no_present(u'品牌分申请-新增list')
        
    def check_Fraction(self):
        self.element_present(u'品牌分申请list')
        
    def select_pending_review(self):
        self.click(u'待审核品牌分list')
        self.switch_frame('frame_0')
        
    def check_pending_review(self):
        self.element_no_present(u'待审核品牌分list')
        
    def save(self):
        self.click(u'提交')
        
    def Check_out(self):
        #return self.find_element(u'品牌分查看list').text
        return self.text(u'品牌分查看list')