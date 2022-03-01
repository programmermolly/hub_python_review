# 要求：创建“老婆”类，创建若干个老婆，统计创建的老婆个数
# 提示：可以用类变量计数

class Wife:
    total_number = 0

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


while True:
    if Wife.total_number >= 3:
        break
    name = input('请输入姓名：')
    height = input('请输入身高：')
    weight = input('请输入体重：')
    w = Wife(name, height, weight)
    Wife.total_number += 1

print('一共创建了%d个对象' % Wife.total_number)
