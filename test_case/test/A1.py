# -*- coding: UTF-8 -*-
class A1(object):
    name = '12233'
    def a1(self,aass,aazz):
        print aass
        print aazz
    def a11(self):
        print A1.name
class A2(A1):
    def b1(self,aazz):
        self.a1('qqqqqq',aazz)
        
aaa = A2()
aaa.b1('edcrfv')
#aaa.a11()

        
