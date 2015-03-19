# -*- coding: UTF-8 -*-
import time
from test_case.PO import BasePage
class xwgl_page(BasePage.Action):
    def main_menu_xwgl(self):
        u'''左边主菜单的选择，公共事务-新闻管理-新闻管理'''
        self.select_main_menu(u'公共事务',u'新闻管理2', u'新闻管理3')
        self.iframe('iframe')
        
    def main_menu_xwll(self):
        u'''左边主菜单的选择，公共事务-新闻管理-新闻浏览'''
        self.select_main_menu(u'公共事务',u'新闻管理2', u'新闻浏览')
        self.iframe('iframe')   
     
    def release(self):
        self.click(u'点击发布')
        self.switch_frame("frame_0")
        self.click(u'确定发布')
        
    def cancel(self):
        self.click(u'点击取消发布')
        self.switch_frame("frame_0")
        self.click(u'确定取消发布')
        
    def title(self,text):
        self.send_keys(u'输入新闻标题', text)
        
    def GxUnitName(self):
        u'''双击打开选择部门'''
        self.double_click(u'双击按部门发布')
        self.switch_frame('frame_1')
        
    def GxUnituser(self):
        u'''通过公司选择发布部门'''
        self.click(u'选择公司')
        self.click(u'选择部门')
        self.click(u'点击确定')
        self.switch_frame('frame_0')
        
    def select_add_list(self):
        u'''单机新增的新闻'''
        self.click(u'选择新增的新闻')
        
    def select_edit_list(self):
        u'''单击编辑后的新闻'''
        self.click(u'选择编辑后的新闻')
        
    def double_list(self):
        u'''双击编辑后的新闻'''
        self.double_click(u'选择编辑后的新闻')
        self.switch_frame('frame_0')
        time.sleep(3)
        
    def category_add_list(self):
        u'''新增新闻是否存在'''
        return self.is_element_present(u'选择新增的新闻')
    
    def category_edit_list(self):
        u'''编辑后的新闻是否存在'''
        return self.is_element_present(u'选择编辑后的新闻')

    def title_text(self):
        return self.text(u"浏览新闻标题")