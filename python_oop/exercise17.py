# 要求：1.定义父类 车
#            数据：品牌、速度
#      2.定义子类：电动车
#             数据：电池容量、充电功率

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class E_car(Car):
    def __init__(self, brand, speed, capacity, power):
        super().__init__(brand, speed)
        self.capacity = capacity
        self.power = power


c01 = Car('Benz', 100)
e01 = E_car('Benz', 100, 200, 50)

print(c01.speed)
# print(c01.capacity) 错误代码！
