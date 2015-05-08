# -*- coding: UTF-8 -*-
import time
from test_case.PO import BasePage
class clgl_page(BasePage.Action):
    def main_menu_cllxgl(self):
        '''公共事务--车辆管理--车辆类型管理'''
        self.select_main_menu(u'公共事务',u'车辆管理',u'车辆类型管理')
        self.iframe('iframe')

    def main_menu_clxxgl(self):
        '''公共事务--车辆管理--车辆信息管理'''
        self.select_main_menu(u'公共事务',u'车辆管理',u'车辆信息管理')
        self.iframe('iframe')
        
    def main_menu_clwhgl(self):
        '''公共事务--车辆管理--车辆维护管理'''
        self.select_main_menu(u'公共事务',u'车辆管理',u'车辆维护管理')
        self.iframe('iframe')
    
    def main_menu_clsysq(self):
        '''公共事务--车辆管理--车辆使用申请'''
        self.select_main_menu(u'公共事务',u'车辆管理',u'车辆使用申请')
        self.iframe('iframe')
        
    def main_menu_clsygl(self):
        '''公共事务--车辆管理--车辆使用管理'''
        self.select_main_menu(u'公共事务',u'车辆管理',u'车辆使用管理')
        self.iframe('iframe')
    
    '''车辆类型管理'''
    def car_type_name(self,text):
        self.send_keys(u'车辆类型名', text)
        
    def select_add_CarType(self):
        self.click(u'新增车辆类型list')
        
    def check_add_CarType(self):
        self.element_present(u'新增车辆类型list')
    
    def select_CarType(self):
        self.click(u'编辑后的车辆类型list')
        
    def check_CarType(self):
        self.element_present(u'编辑后的车辆类型list')
        
    def check_CarType_no(self):
        self.element_no_present(u'编辑后的车辆类型list')
        
    '''车辆信息管理'''
    def select_car(self):
        self.click(u'车辆0901304Alist')

    def check_car(self):
        self.element_present(u'车辆0901304Alist')
        
    def check_car_no(self):
        self.element_no_present(u'车辆0901304Alist')

    def send_CarNum(self,text):
        self.send_keys(u'车牌号', text)
        
    def CarModel(self,text):
        self.send_keys(u'厂牌型号', text)
        
    def CarType(self):
        self.double_click(u"车辆类型")
        self.switch_frame('frame_1')
        
    def CarPrice(self,text):
        self.send_keys(u"车辆价格",text)
        
    def Status(self,text):
        '''
                共有四个状态
            1、可用车辆 2、已损坏 3、维修中 4、已报废
        '''
        self.down_box(u"当前状态",text)


    def tab_kycl(self):
        self.click(u'可用车辆tab')
        
    def tab_ysh(self):
        self.click(u'已损坏tab')
        
    def tab_wxz(self):
        self.click(u'维修中tab')
    
    def tab_ybf(self):
        self.click(u'已报废tab')
        
    def double_carnum(self):
        self.double_click(u'车牌号')
        self.switch_frame('frame_1')
        
    def RepairTime(self,text):
        self.send_keys(u'维护日期', text)
        
    def RepairType(self,text):
        self.down_box(u'维护类型', text)
        
    def jiayou(self,text):
        self.send_keys(u"加油升数", text)
        
    def StartTime(self,text):
        self.send_keys(u'车辆使用开始时间', text)
        self.click(u'点击时间确定')
        
    def EndTime(self,text):
        self.send_keys(u'车辆使用结束时间', text)
        self.click(u'点击时间确定')
        
    def Destination(self,text):
        self.send_keys(u'目的地',text)
        
    def Miles(self,text):
        self.send_keys(u'里程',text)
        
    def ManagerName(self):
        self.double_click(u'调度员框')
        self.switch_frame('frame_2')
        
    def select_Manager(self):
        self.click(u'调度员')
        
    def tab_ytg(self):
        self.click(u'已通过')
        
    def tab_syz(self):
        self.click(u'使用中')
        
    def approval(self):
        '''选中鲁A-0901304A车，并点击审批'''
        self.click(u'审批')
        self.switch_frame("frame_0")
        
    def use_car(self):
        '''选中鲁A-0901304A车，并点击使用'''
        self.click(u'使用')
        self.click(u"操作确认")
        
    def end_use(self):
        '''选中鲁A-0901304A车，并点击结束'''
        self.click(u'结束')
        self.click(u"操作确认")
        