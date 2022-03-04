# 要求：用面向对象的思想描述下列语句：
# 张无忌教赵敏九阳神功
# 赵敏教张无忌化妆
# 张无忌一个月10000元
# 赵敏一个月6000元

class Person:
    def __init__(self,name,money):
        self.name=name
        self.money=money
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    def teaching(self,others,content):
        print(self.name,'教',others.name,content)

    def making_money(self,value):
        print('%s赚了%d元'%(self.name,value))


zwj=Person('zwj',10000)
zm=Person('zm',6000)
zwj.teaching(zwj,'jiuyangshengong')
zm.making_money(6000)
zwj.making_money(10000)




