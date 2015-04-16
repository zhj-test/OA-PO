# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from test_case.PO.page_ggsw import clgl_page
from test_case.PO import public_page

class case_clgl(unittest.TestCase):
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

        self.clgl = clgl_page.clgl_page(self.driver)
        self.public = public_page.public_page(self.driver)

        self.public.login('ycadmin','111111')
        
    def test_case(self):
        '''
        self.cllxgl_xz()
        self.cllxgl_bj()
        self.clxxgl_xz()
        self.clxxgl_bj_ysh()
        self.clxxgl_bj_wxz()
        self.clxxgl_bj_ybf()
        self.clxxgl_bj_kycl()
        self.clwhgl_xz()
        self.clwhgl_bj()
        self.clwhgl_sc()
        '''
        self.clsysq_xz()
        self.clsygl_sp()
        self.clsysq_sy()
        self.clsysq_js()
        
        self.clxxgl_sc()
        self.cllxgl_sc()
        self.public.quit()
    
    def cllxgl_xz(self):
        print u'<---------------车辆类别新增--------------->'
        self.clgl.main_menu_cllxgl()
        self.public.add()
        self.clgl.car_type_name(u"商务车")
        self.public.submit()
        self.clgl.check_add_CarType()
        
    def cllxgl_bj(self):
        print u'<---------------车辆类别修改--------------->'
        self.clgl.main_menu_cllxgl()
        self.clgl.select_add_CarType()
        self.public.edit()
        self.clgl.car_type_name('SUV')
        self.public.submit()
        self.clgl.check_CarType()
        
    def clxxgl_xz(self):
        print u'<---------------车辆信息新增--------------->'
        self.clgl.main_menu_clxxgl()
        self.public.add()
        self.clgl.send_CarNum(u'鲁A-0901304A')
        self.clgl.CarModel(u'奥迪A6')
        self.clgl.CarPrice('999')
        self.clgl.CarType()
        self.clgl.select_CarType()
        self.public.ok()
        self.public.submit()
        self.clgl.check_car()
        
    def clxxgl_bj_ysh(self):
        print u'<---------------将车辆状态修改为已损坏--------------->'
        '''将车辆状态修改为已损坏'''
        self.clgl.main_menu_clxxgl()
        self.clgl.select_car()
        self.public.edit()
        self.clgl.Status(u'损坏')
        self.public.submit()
        self.clgl.check_car_no()
      
    def clxxgl_bj_wxz(self):
        print u'<---------------将车辆状态修改为维修中--------------->'
        '''将车辆状态修改为维修中'''
        self.clgl.main_menu_clxxgl()
        self.clgl.tab_ysh()
        self.clgl.select_car()
        self.public.edit()
        self.clgl.Status(u'维修中')
        self.public.submit()
        self.clgl.check_car_no()
        
    def clxxgl_bj_ybf(self):
        print u'<---------------将车辆状态修改为已报废--------------->'
        '''将车辆状态修改为已报废'''
        self.clgl.main_menu_clxxgl()
        self.clgl.tab_wxz()
        self.clgl.select_car()
        self.public.edit()
        self.clgl.Status(u'报废')
        self.public.submit()
        self.clgl.check_car_no()
        
    def clxxgl_bj_kycl(self):
        print u'<---------------将车辆状态修改为可用车辆--------------->'
        '''将车辆状态修改为可用车辆'''
        self.clgl.main_menu_clxxgl()
        self.clgl.tab_ybf()
        self.clgl.select_car()
        self.public.edit()
        self.clgl.Status(u'可用')
        self.public.submit()
        self.clgl.check_car_no()
    
    def clwhgl_xz(self):
        print u'<---------------车辆维护管理-新增--------------->'
        self.clgl.main_menu_clwhgl()
        self.public.add()
        self.clgl.double_carnum()
        self.clgl.select_car()
        self.public.ok()
        self.clgl.RepairTime('2015-01-02')
        self.clgl.RepairType(u'维修')
        self.public.submit()
        self.clgl.check_car()
        
    def clwhgl_bj(self):
        print u'<---------------车辆维护管理-编辑--------------->'
        self.clgl.main_menu_clwhgl()
        self.clgl.select_car()
        self.public.edit()
        self.clgl.RepairType(u'加油')
        self.clgl.jiayou('99')
        self.public.submit()
        self.clgl.check_car()
        
    def clsysq_xz(self):
        print u'<---------------车辆使用申请-新增--------------->'
        self.clgl.main_menu_clsysq()
        self.public.add()
        self.clgl.double_carnum()
        self.clgl.select_car()
        self.public.ok()
        self.clgl.StartTime('2015-03-01 15:50')
        self.clgl.EndTime('2015-03-03 15:50')
        self.clgl.Destination(u'北京')
        self.clgl.Miles('9999')
        self.clgl.ManagerName()
        self.clgl.select_Manager()
        self.public.ok()
        self.public.submit()
        self.clgl.check_car()
        
    def clsygl_sp(self):
        print u'<---------------车辆使用管理-审批--------------->'
        self.clgl.main_menu_clsygl()
        self.clgl.approval()
        self.public.submit()
        self.driver.refresh()
        
    def clsysq_sy(self):
        print u'<---------------车辆使用申请-使用--------------->'
        self.clgl.main_menu_clsysq()
        self.clgl.tab_ytg()
        self.clgl.use_car()
        self.driver.refresh()
        
    def clsysq_js(self):
        print u'<---------------车辆使用申请-结束--------------->'
        self.clgl.main_menu_clsysq()
        self.clgl.tab_syz()
        self.clgl.end_use()
        self.driver.refresh()
        
    def clwhgl_sc(self):
        print u'<---------------车辆维护管理-删除--------------->'
        self.clgl.main_menu_clwhgl()
        self.clgl.select_car()
        self.public.delete()
        self.clgl.check_car_no()
        
    def clxxgl_sc(self):
        print u'<---------------将车辆信息管理-删除--------------->'
        '''将车辆状态修改为已损坏'''
        self.clgl.main_menu_clxxgl()
        self.clgl.select_car()
        self.public.delete()
        self.driver.refresh()
        self.clgl.check_car_no()
        
    def cllxgl_sc(self):
        print u'<---------------车辆类别-删除--------------->'
        self.clgl.main_menu_cllxgl()
        self.clgl.select_CarType()
        self.public.delete()
        self.clgl.check_CarType_no()
        
       
if __name__ == "__main__":
    unittest.main()  