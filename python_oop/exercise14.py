# 要求：请用面向对象的思想，描述下列语句：
# 小明在招商银行取钱

class Person:
    def __init__(self, name, money=0):
        self.name = name
        self.money = money
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,money):
        self.__money=money




class Bank:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def withdraw_money(self, value, person):
        print('%s取%d钱！' % (person.name, value))


person = Person('xm')
bank = Bank('zsyh', 100000)
bank.withdraw_money(1000, person)
