# -*- coding: UTF-8 -*-
import time
import yaml
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Action(object):
    
    def __init__(self,driver):
        self.driver = driver
        self.B_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        
    def get_value(self,key):
        #通过yaml文件获取定位信息
        file_path = os.path.join(self.B_DIR,"data","location_element.yaml")
        f = open(file_path)
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
        '''
                        判断运行是否成功：
            1、若成功，输出运行成功；
            2、若不成功，则对失败页面进行屏幕截图，并保存:
               (1)保存路径为'screenshot'--day_now--Name_time_now.png;
               (2)保存前先判断'screenshot'文件夹下是否存在day_now文件夹，若不存在，则先新建'day_now'文件夹
               (3)保存的文件名为    “所检查的操作名Name”_“所检查的时间time_now”.png
        '''
        #判断运行是否成功
        if isSucceed:
            print  Name + u"：运行成功！"
        else:
            day_now = time.strftime("%Y%m%d",time.localtime(time.time()))
            time_now = time.strftime("%H%M%S",time.localtime(time.time()))
            path = os.path.join(self.B_DIR,'screenshot',day_now)
            if not os.path.exists(path):
                os.mkdir(path)
            png_path = os.path.join(path,Name+ "_"+ time_now+ '.png')
            self.capture_screenshot(png_path)
            print  Name + u"：运行失败！请查看截图快照："+ png_path
            self.driver.quit()
            
    def open(self,key):
        #打开浏览器--输入网址--将浏览器最大化
        data = self.get_value(key)
        self.driver.get(data[0])
        self.driver.maximize_window()
        time.sleep(2)

    def find_element(self,key):
        #定位一个元素：与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        data = self.get_value(key)
        try:
            element=WebDriverWait(self.driver, 10).until(lambda driver :driver.find_element(data[0],data[1]))
            return element
        except BaseException, e:
            self.operation_check(key+ u'元素未发现',False)
            print e
     
    def find_elements(self,key):
        #定位一组元素：与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        data = self.get_value(key)
        isSucceed = False
        try:
            if len(self.driver.find_elements(data[0],data[1])):
                return self.driver.find_elements(data[0],data[1])
                isSucceed = True
        except BaseException, e:
            print e
        self.operation_check(key+ u'元素未发现',isSucceed)
    
    def send_keys(self,key,text,clear=True,click=True):
        '''
                    在输入框内输入内容：
            1、clear=True：清除输入框的内容
            2、click=True：对文本框进行一个单机操作，再进行输入
        '''
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
        self.operation_check(u'输入 <'+ key+ u'> 操作',isSucceed)
        
    def click(self,key):
        #鼠标左键单击操作，
        isSucceed = False
        aaa = self.find_element(key)
        try:
            aaa.click()
            isSucceed = True
        except BaseException, e:
            print e
    
        self.operation_check(u'点击 <'+ key+ u'> 操作',isSucceed)
        
    def double_click(self,key):
        #鼠标左键双击操作
        isSucceed = False
        #定位到要悬停的元素
        click = self.find_element(key)
        try:
            ActionChains(self.driver).double_click(click).perform()
            isSucceed = True
        except BaseException, e:
            print e
        
        self.operation_check(u"双击 <"+ key+ u'> 操作',isSucceed)
        
    def switch_to_frame(self,frame):
        #重写switch_frame方法
        time.sleep(1)
        try:
            self.driver.switch_to_frame(frame)
            time.sleep(0.5)
        except BaseException, e:
            print e

    def switch_frame(self, frame):
        #先退出所有frame，再次进入新的frame
        #isSucceed = False
        try:
            self.driver.switch_to_default_content()     #退出frame，切换到新的frame
            self.switch_to_frame(frame)
            #isSucceed = True
        except BaseException, e:
            print e
        #self.operation_check(u'切换到'+ frame,isSucceed)
        
    def iframe(self,key):
        #进入frame：针对frame没有id、neme属性的
        #isSucceed = False
        self.driver.switch_to_default_content()
        frame = self.find_element(key)
        try:
            self.driver.switch_to_frame(frame)
            #isSucceed = True
        except BaseException, e:
            print e    
        #self.operation_check(u'切换到主页面'+ key,isSucceed)
        
    def text(self,key):
        #获取文本值
        return self.find_element(key).text
        
    def select_main_menu(self,key1,key2,key3):
        if key1 == u'选择个人事务':
            #个人事务模块的选择
            self.find_element(key2).click()
            self.find_element(key3).click()
        else:
            self.find_element(key1).click()
            self.find_element(key2).click()
            self.find_element(key3).click()
               
    def execute_script(self,key):
        #调用JavaScript
        data = self.get_value(key)
        isSucceed = False
        try:
            self.driver.except_script(data)
            isSucceed = True
        except BaseException, e:
            print e
        
        self.operation_check(key,isSucceed)
    
    def down_box(self,key,text):
        u'''通过可见文本选择下拉框中的值'''
        data = self.get_value(key)
        isSucceed = False
        try:
            WebDriverWait(self.driver, 3,0.5).until(lambda driver: driver.find_element(data[0],data[1]))
            select = Select(self.driver.find_element(data[0],data[1]))
            select.select_by_visible_text(text)
            isSucceed = True
        except BaseException, e:
            print e
        self.operation_check(u'下拉框中选择: <'+ text+ u'> 操作',isSucceed)
        
            
    def element_present(self,key):
        #检查页面上的元素是否新增或编辑成功
        data = self.get_value(key)
        isSucceed = False
        try:
            element=WebDriverWait(self.driver, 3).until(lambda driver :driver.find_element(data[0],data[1]))
            element.click()
            isSucceed = True
            self.operation_check(u'列表中存在<'+ key+ u'>数据',isSucceed) 
        except BaseException, e:
            self.operation_check(u'列表中不存在<'+ key+ u'>数据',isSucceed)
            print e
        finally:  
            print u'<---------------本条用例运行结束--------------->'
            print ''
            self.driver.refresh()
            
        
    def element_no_present(self,key):
        #检查页面上的元素删除后是否还存在
        data = self.get_value(key)
        isSucceed = False
        try:
            element=WebDriverWait(self.driver, 2).until(lambda driver :driver.find_element(data[0],data[1]))
            element.click()
            self.operation_check(u'执行删除后，列表中仍存在<'+ key+ u'>数据',isSucceed)
        except:
            isSucceed = True
            self.operation_check(u'执行删除后，列表中已不存在<'+ key+ u'>数据',isSucceed)
            self.driver.refresh()
        finally:  
            print u'<---------------本条用例运行结束--------------->'
            print ''

        