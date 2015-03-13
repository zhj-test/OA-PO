# -*- coding: UTF-8 -*-
import time
import yaml
from test_case.PO import BasePage
class public_page(BasePage.Action):
    def input_data(self,key):
        #通过yaml文件获取数据
        f = open('E:\\script\\myselenium\\OA-PO\\data\\input_data.yaml')
        value = yaml.load(f)
        f.close()
        try:
            data = value[key]
            return data    
        except KeyError:
            print 'location_element文件中找不到%s' %key
    
    def login(self,name,password):
        self.send_keys(u'输入登陆用户名',name)
        self.send_keys(u'输入登录密码',password)
        self.click(u'点击登录')
    
    def add(self):
        self.click('点击新增')
        self.switch_frame("frame_0")
        
    def delete(self):
        self.click('点击删除')
        time.sleep(1)
        self.click('确定删除')
        
    def edit(self):
        self.click('点击编辑')
        self.switch_frame("frame_0")
    
    def quert(self):
        self.click('点击查询')
        
    def submit(self):    
        self.click('点击提交')
    
    def close(self):
        self.click('点击关闭')
        
    def ueditor(self,key,text,ueditor='ueditor_0'): 
        self.switch_frame(ueditor)
        self.send_keys(u'富文本框',text)
        time.sleep(1)
        self.switch_frame('frame_0')
        
    def quit(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        print u"+用例运行完毕退出"