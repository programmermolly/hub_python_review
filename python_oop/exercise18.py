# 要求：体会面向对象编程的三大特征：封装、继承、多态
# 1.定义图形管理器，管理所有图形
# 2.定义计算面积的方法
# 图形包括：圆形、矩形
# 注意：添加新图形不能修改图形管理器的代码

class ShapeManager:
    def calculate_area(self):
        pass


class Circle(ShapeManager):
    def __init__(self, r):
        self.radius = r

    def calculate_area(self):
        return self.radius ** 2 * 3.14


class Rectangle(ShapeManager):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


rec = Rectangle(10, 20)
print(rec.calculate_area())
cir = Circle(10)
print(cir.calculate_area())
