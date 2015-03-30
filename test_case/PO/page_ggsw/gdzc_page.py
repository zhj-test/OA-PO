# -*- coding: UTF-8 -*-
import time
from test_case.PO import BasePage
class gdzc_page(BasePage.Action):
    def main_menu_gdzcgl(self):
        '''公共事务--固定资产--固定资产管理'''
        self.select_main_menu(u'公共事务',u'固定资产',u'固定资产管理')
        self.iframe('iframe')
        
    def main_menu_zczjgl(self):
        '''公共事务--固定资产--资产折旧管理'''
        self.select_main_menu(u'公共事务',u'固定资产',u'资产折旧管理')
        self.iframe('iframe')
    
    def main_menu_rwlbsz(self):
        '''公共事务--固定资产--任务类别设置'''
        self.select_main_menu(u'公共事务',u'固定资产',u'任务类别设置')
        self.iframe('iframe')
        
    def main_menu_gdzclb(self):
        '''公共事务--固定资产--固定资产类别'''
        self.select_main_menu(u'公共事务',u'固定资产',u'固定资产类别')
        self.iframe('iframe')
    
    def main_menu_zjzclb(self):
        '''公共事务--固定资产--折旧资产类别'''
        self.select_main_menu(u'公共事务',u'固定资产',u'折旧资产类别')
        self.iframe('iframe')
        
    def type_name(self,text):
        self.send_keys(u'资产类别名称', text)
        
    def select_add_type(self):
        self.click(u'新增资产类别list')
        
    def select_type(self):
        self.click(u'选择资产类别list')
        
    def DepType(self,text):
        self.send_keys(u'折旧资产类别', text)
        
    def DepRate(self,text):
        self.send_keys(u'折旧率', text)
        
    def DepCycle(self,text):
        self.send_keys(u'折旧周期', text)
        
    def select_add_DepType(self):
        self.click('新增折旧资产类别list')
    
    def select_DepType(self):
        self.click('选择折旧资产类别list')
        
    def Task_type_name(self,text):
        self.send_keys(u'任务类型名', text) 
        
    def select_add_task(self):
        self.click(u'新增--任务类型名list')
        
    def select_task(self):
        self.click(u'主线任务list')
        
    def Asset_Number(self,text):
        self.send_keys(u'资产编号', text)
        
    def Asset_name(self,text):
        self.send_keys(u'资产名称', text)
        
    def AssetModel(self,text):
        self.send_keys(u'规格型号', text)
        
    def AssetType(self):
        self.double_click(u'资产类别')
        self.switch_frame('frame_1')
        self.click('选择资产类别list')
        self.click('点击确定')
    
    def double_DepType(self):
        self.double_click(u'折旧类别')
        self.switch_frame('frame_1')
        self.click('选择折旧资产类别list')
        self.click('点击确定')
        
    def DepStartDate(self,text):
        self.send_keys(u'开始折旧日期', text)
        
    def ActualMoney(self,text):
        self.send_keys(u'资产原值', text)
        
    def MinMoney(self,text):
        self.send_keys(u'资产最低值', text)
        
    def select_add_Asset(self):
        self.click(u"新增固定资产list")
        
    def select_Asset(self):
        self.click(u"固定资产list")

        

    