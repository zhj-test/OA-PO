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
            print u'location_element文件中找不到%s' %key
    
    def login(self,name,password):
        self.open(u'url地址')
        print ''
        self.send_keys(u'输入登陆用户名',name)
        self.send_keys(u'输入登录密码',password)
        self.click(u'点击登录')
    
    def add(self):
        self.click(u'点击新增')
        self.switch_frame("frame_0")
        
    def delete(self):
        self.click(u'点击删除')
        time.sleep(1)
        self.click(u'确定删除')
        self.iframe('iframe')
        time.sleep(3)
        
    def edit(self):
        self.click(u'点击编辑')
        #time.sleep(3)
        self.switch_frame("frame_0")
    
    def quert(self):
        self.click(u'点击查询')
        
    def submit(self):    
        self.click(u'点击提交')
        #self.iframe('iframe')
        print ''
        time.sleep(2)
        self.driver.refresh()
        
    
    def close(self):
        self.click(u'点击关闭')
        
    def ok(self):
        self.click(u'点击确定')
        self.switch_frame('frame_0')
        
    def ueditor(self,text,ueditor='ueditor_0'):
        self.driver.switch_to_frame(ueditor) 
        #self.switch_frame(ueditor)
        self.send_keys(u'富文本框',text)
        time.sleep(1)
        self.switch_frame('frame_0')
        
    def quit(self):
        print u"---------------所有用例运行完毕退出---------------"
        self.driver.quit()
        #self.assertEqual([], self.verificationErrors)
        
    
    def error_quit(self):
        print u"该条用例数据验证失败，退出"
        self.driver.quit()
        raise IndexError
    

        
        
        
        