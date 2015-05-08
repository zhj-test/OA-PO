# -*- coding: UTF-8 -*-
from test_case.PO import BasePage
class login_page(BasePage.Action):

    def open_url(self):
        self.open(u'url地址')
        
    def name(self,text):
        self.send_keys('输入登陆用户名', text)
        
    def TxtName(self,name):
        self.send_keys(u'输入登陆用户名',name)
        
    def TxtPwd(self,password):
        self.send_keys(u'输入登录密码',password)
        
    def login_button(self):
        self.click(u'点击登录')
        
    def errot_mtip(self):
        return self.find_element(u'错误信息提示')
             
    def login(self,name,password):
        self.open_url()
        self.TxtName(name)
        self.TxtPwd(password)
        self.login_button()
