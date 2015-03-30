# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from test_case.PO.page_ggsw import gdzc_page
from test_case.PO import public_page

class case_gdzc(unittest.TestCase):
    def setUp(self):
        u'''
                初始化用例
                实例化Page类
                实现登录
        '''
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

        self.gdzc = gdzc_page.gdzc_page(self.driver)
        self.public = public_page.public_page(self.driver)

        self.public.login('ycadmin','111111')
        
    def test_gdzc(self):
        self.gdzclb_xz()
        self.gdzclb_bj()
        
        self.zjzclb_xz()
        self.zjzclb_bj()
        
        self.rwlxsz_xz()
        self.rwlxsz_bj()
        
        self.gdzcgl_xz()
        self.gdzcgl_bj()
        
        self.gdzcgl_sc()
        self.rwlbsz_sc()
        self.zjzclb_sc()
        self.gdzclb_sc()
        
    def gdzclb_xz(self):
        print u'<---------------固定资产类别-新增--------------->'
        self.gdzc.main_menu_gdzclb()
        self.public.add()
        self.gdzc.type_name(u'新增--军火类')
        self.public.submit()
        
    def gdzclb_bj(self):
        print u'<---------------固定资产类别-编辑--------------->'
        self.gdzc.main_menu_gdzclb()
        self.gdzc.select_add_type()
        self.public.edit()
        self.gdzc.type_name(u'计算机周边')
        self.public.submit()
        
    def zjzclb_xz(self):
        print u'<---------------折旧资产类别-新增--------------->'
        self.gdzc.main_menu_zjzclb()
        self.public.add()
        self.gdzc.DepType('新增--运输损坏')
        self.gdzc.DepRate('9')
        self.gdzc.DepCycle('11')
        self.public.submit()
        
    def zjzclb_bj(self):
        print u'<---------------折旧资产类别-编辑--------------->'
        self.gdzc.main_menu_zjzclb()
        self.gdzc.select_add_DepType()
        self.public.edit()
        self.gdzc.DepType(u'使用损耗')
        self.public.submit()
        
    def rwlxsz_xz(self):
        print u'<---------------任务类别设置-新增--------------->'
        self.gdzc.main_menu_rwlbsz()
        self.public.add()
        self.gdzc.Task_type_name(u'新增--任务类型名')
        self.public.submit()
        
    def rwlxsz_bj(self):
        print u'<---------------任务类别设置-编辑--------------->'
        self.gdzc.main_menu_rwlbsz()
        self.gdzc.select_add_task()
        self.public.edit()
        self.gdzc.Task_type_name(u'主线任务')
        self.public.submit()
        
    def gdzcgl_xz(self):
        print u'<---------------固定资产管理-新增--------------->'
        self.gdzc.main_menu_gdzcgl()
        self.public.add()
        self.gdzc.Asset_Number(u'新增-JNDZ-304A')
        self.gdzc.Asset_name(u'U盘')
        self.gdzc.AssetModel(u'个')
        self.gdzc.AssetType()
        self.gdzc.double_DepType()
        self.gdzc.DepStartDate('2014-3-24')
        self.gdzc.ActualMoney('999')
        self.gdzc.MinMoney('99')
        self.public.submit()
        
    def gdzcgl_bj(self):
        print u'<---------------固定资产管理-新增--------------->'
        self.gdzc.main_menu_gdzcgl()
        self.gdzc.select_add_Asset()
        self.public.edit()
        self.gdzc.Asset_Number(u'U-304A')
        self.public.submit()
        
    #资产折旧管理，无法操作，未写用例
    
    
    def gdzcgl_sc(self):
        print u'<---------------固定资产管理-删除--------------->'
        self.gdzc.main_menu_gdzcgl()
        self.gdzc.select_Asset()
        self.public.delete()
        self.driver.refresh()
        
    def rwlbsz_sc(self):
        print u'<---------------任务类别设置-删除--------------->'
        self.gdzc.main_menu_rwlbsz()
        self.gdzc.select_task()
        self.public.delete()
        self.driver.refresh()
        
    def zjzclb_sc(self):
        print u'<---------------折旧资产类别-删除--------------->'
        self.gdzc.main_menu_zjzclb()
        self.gdzc.select_DepType()
        self.public.delete()
        self.driver.refresh()
        
    def gdzclb_sc(self):
        print u'<---------------固定资产类别-删除--------------->'
        self.gdzc.main_menu_gdzclb()
        self.gdzc.select_type()
        self.public.delete()
        self.driver.refresh()
    
if __name__ == "__main__":
    unittest.main()      