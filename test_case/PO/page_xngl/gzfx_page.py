# -*- coding: UTF-8 -*-
import time
from test_case.PO import BasePage
class gzfx_page(BasePage.Action):
    def main_menu_gzfx(self):
        '''效能管理--工作分享--工作分享'''
        self.select_main_menu(u'效能管理',u'工作分享1',u'工作分享2')
        self.iframe('iframe')
        
    def main_menu_fxqsz(self):
        '''效能管理--工作分享--分享区设置'''
        self.select_main_menu(u'效能管理',u'工作分享1',u'分享区设置')
        self.iframe('iframe')
    
    def main_menu_gzrsz(self):
        '''效能管理--工作分享--关注人设置'''
        self.select_main_menu(u'效能管理',u'工作分享1',u'关注人设置')
        self.iframe('iframe')
        
    def main_menu_fxwh(self):
        '''效能管理--工作分享--分享维护'''
        self.select_main_menu(u'效能管理',u'工作分享1',u'分享维护')
        self.iframe('iframe')  
        
    def ShareArea(self,text):
        self.send_keys(u'分享区名称', text)
        
    def select_add_ShareArea(self):
        self.click(u'分享区-新增list')
    
    def select_ShareArea(self):
        self.click(u'分享区list')
        
    def select_company(self):
        self.click(u'管理人员公司')
        
    def select_user(self):
        return self.find_elements(u'选择分享人')
    
    def select_all(self):
        time.sleep(2)
        self.click(u'全选')
    
    def Unselect_all(self):
        time.sleep(2)
        self.click(u'全不选')
        
    def tab_wfbd(self):
        self.click(u'我发布的tab')
        
    def ShareTheme(self,text):
        self.send_keys(u'分享主题', text)
        
    def Share_Area(self):
        self.click(u'分享区选择框')
        self.click(u'分享区')
        
    def share_content(self,text):
        self.send_keys(u'分享内容', text)
        
    def select_add_jobshare(self):
        self.click('新增工作分享list')

    def select_jobshare(self):
        self.click('工作分享list')
        
    