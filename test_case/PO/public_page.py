# -*- coding: UTF-8 -*-
import time,os
import yaml
from test_case.PO import BasePage
class public_page(BasePage.Action):
 
    def input_data(self,key):
        #通过yaml文件获取数据
        file_path = os.path.join(self.B_DIR,"data","location_element.yaml")
        f = open(file_path)
        #f = open('E:\\script\\myselenium\\OA-PO\\data\\input_data.yaml')
        value = yaml.load(f)
        f.close()
        try:
            data = value[key]
            return data    
        except KeyError:
            print u'location_element文件中找不到%s' %key
    
    def login(self,name,password):
        #登录操作
        self.open(u'url地址')
        print ''
        self.send_keys(u'输入登陆用户名',name)
        self.send_keys(u'输入登录密码',password)
        self.click(u'点击登录')
        print ''
    
    def add(self):
        self.click(u'点击新增')
        self.switch_frame("frame_0")
        
    def delete(self):
        self.click(u'点击删除')
        time.sleep(1)
        self.click(u'确定删除')
        self.iframe('iframe')
        time.sleep(1)
        
    def edit(self):
        self.click(u'点击编辑')
        time.sleep(3)
        self.switch_frame("frame_0")
    
    def quert(self):
        self.click(u'点击查询')
        
    def submit(self):    
        self.click(u'点击提交')
        self.iframe('iframe')

    def close(self):
        self.click(u'点击关闭')
        
    def ok(self):
        self.click(u'点击确定')
        self.switch_frame('frame_0')
        
        
    def ueditor(self,text,ueditor='ueditor_0'):
        self.driver.switch_to_frame(ueditor) 
        self.send_keys(u'富文本框',text)
        time.sleep(1)
        self.switch_frame('frame_0')
        
    def Upload(self):
        '''
        1、上传功能
        2、调用的upfile.exe，由AutoIt,生成，使用文档存放在test_doc文件下
        3、上传的文档地址为："我的电脑--库--图片--示例图片" 中的 <灯塔.jpg>(W7默认存在),若没有该图片，请添加，或修改upfile.exe
        4、调用的upfile.exe与生成upfile.exe的脚本upfile.au3存放在..\data\Upload文件夹中
        '''
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        file_path = os.path.join(BASE_DIR,"data","Upload","upfile.exe")
        #Python 的os模块的system()方法可以调用exe程序并执行
        os.system(file_path)
        time.sleep(10)
        
    def quit(self):
        print u"^_^ ^_^ ^_^ ^_^ 所有用例运行完毕 !^_^! 退出 ^_^ ^_^ ^_^ ^_^"
        self.driver.quit()
