# -*- coding: UTF-8 -*-
import time
import yaml
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Action(object):
    def __init__(self,driver):
        self.driver = driver
    def get_value(self,key):
        #通过yaml文件获取定位信息
        f = open('E:\\script\\myselenium\\OA-PO\\data\\location_element.yaml')
        value = yaml.load(f)
        f.close()
        try:
            data = value[key]
            return data
        except KeyError:
            print 'location_element文件中找不到%s' %key

    def capture_screenshot(self,filename):
        #截取屏幕截图并保存到指定路径
        try:
            self.driver.get_screenshot_as_file(filename)
        except BaseException, e:
            print "保存屏幕截图失败，失败信息:"+ e

    def operation_check(self,Name,isSucceed):
        #判断运行是否成功
        if isSucceed:
            print  Name + u"操作：运行成功！"
        else:
            day_now = time.strftime("%Y%m%d",time.localtime(time.time()))
            time_now = time.strftime("%H%M%S",time.localtime(time.time()))
            if os.path.exists("E:\\script\\myselenium\\OA-PO\\screenshot\\" + day_now):
                pass
            else:
                os.mkdir("E:\\script\\myselenium\\OA-PO\\screenshot\\" + day_now)
            captureName = "E:\\script\\myselenium\\OA-PO\\screenshot\\" + day_now+  "\\"+ Name+ "_"+ time_now+ '.png'
            #调用capture_screenshot()保存运行失败时的屏幕截图
            self.capture_screenshot(captureName)
            print  Name + u"操作：运行失败！请查看截图快照："+ captureName
            
    def open(self,key):
        data = self.get_value(key)
        self.driver.get(data)
        self.driver.maximize_window()
        time.sleep(2)

    def find_element(self,key):
        #定位一个元素：与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        data = self.get_value(key)
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(data[0],data[1]).is_displayed())
            return self.driver.find_element(data[0],data[1])
        #logging.debug(time.ctime()+ "find element [" + str(by) + "] success")
        except BaseException, e:
            self.operation_check(key,False)
            print e
        
        
    def find_elements(self,key):
        #定位一组元素：与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        data = self.get_value(key)
        isSucceed = False
        try:
            if len(self.driver.find_elements(data[0],data[1])):
                return self.driver.find_elements(data[0],data[1])
                isSucceed = True
        #logging.debug(time.ctime()+ "find element [" + str(by) + "] success")
        except BaseException, e:
            print e
        self.operation_check("find_elements",isSucceed)
    
    def send_keys(self,key,text,clear=True, click=True):
        #内容重新输入:清理指定对象中已经输入的内容重新输入，操作之前自动等待到对象可见。
        isSucceed = False
        send = self.find_element(key)
        if click:
            send.click()
        if clear:
            send.clear()
        try:
            send.send_keys(text)
            isSucceed = True
        except BaseException, e:
            print e
        self.operation_check(u'输入'+ key,isSucceed)
        
    def click(self,key):
        
        isSucceed = False
        send = self.find_element(key)
        try:
            send.click()
            isSucceed = True
        except BaseException, e:
            print e
        
        self.operation_check(u'点击'+ key,isSucceed)
        
    def double_click(self,key):
        isSucceed = False
        try:
            #定位到要悬停的元素
            click = self.driver.find_element(key)
            ActionChains(self.driver).double_click(click).perform()
            isSucceed = True
        except BaseException, e:
            print e
        
        self.operation_check(u"双击"+ key,isSucceed)

    def switch_frame(self, frame):
        #重写switch_frame方法
        isSucceed = False
        try:
            self.driver.switch_to_default_content()      #退出frame，切换到新的frame
            return self.driver.switch_to_frame(frame)
        except BaseException, e:
            print e
        self.operation_check('iframe切换',isSucceed)
        
    def iframe(self,key):
        isSucceed = False
        try:
            self.driver.switch_to_default_content()
            frame = self.find_element(key)#('xpath',"//html/body/div[@class='panel layout-panel layout-panel-center']/div/div/div[@class='tabs-panels']/div[2]/div/div/iframe")
            self.driver.switch_to_frame(frame)
            isSucceed = True
        except BaseException, e:
            print e    
        self.operation_check(key,isSucceed)
        
    def select_main_menu(self,key1,key2,key3):
        if key1 == u'选择个人事务':
            #个人事务模块的选择
            self.click(key2)
            self.click(key3)
        else:
            self.click(key1)
            self.click(key2)
            self.click(key3)
               
    def execute_script(self,key):
            #调用JavaScript
        isSucceed = False
        try:
            self.driver.except_script(key)
            isSucceed = True
        except BaseException, e:
            print e
        
        self.operation_check(key,isSucceed)
        
    def is_element_present(self,key):
        #检查页面上的元素是否存在
        data = self.get_value(key)
        try:
            self.driver.find_element(data[0],data[1])
            return True
        except:
            return False
        