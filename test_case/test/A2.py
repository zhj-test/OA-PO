# -*- coding: UTF-8 -*-
import yaml
def get_value(key):
    #通过yaml文件获取定位信息
    f = open('E:\\script\\myselenium\\OA-PO\\data\\location_element.yaml')
    value = yaml.load(f)
    f.close()
    try:
        data = value[key]
        return data
    except KeyError:
        print 'location_element文件中找不到%s' %key
get_value(u'url地址')
