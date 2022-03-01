# 要求：在二位列表中查找元素（指定位置、方向、步数）
# list_given=[
#     ['00','01','02','03'],
#     ['10','11','12','13'],
#     ['20','21','22','23'],
# ]
# 1.'13'位置向左3个元素
# 2.'22'位置向上两个元素
# 3.'03'位置向下两个元素
# 提示：1.可用坐标表示位置，坐标的运算表示位置变化
#      2.给定的列表是二维列表，命名时需注意
#      3.建议将结果存到列表里

# 创建类
class Vector2:
    """
    辅助获取二维列表元素的类
    """
    def __init__(self, x, y):
        """
        初始化类
        :param x: 外索引
        :param y: 内索引
        """
        self.x = x
        self.y = y
    # 表示方向
    @staticmethod
    def left():
        return  Vector2(0, -1)

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)



def get_elements(map_given,pos_given,dir_given,count):
    """
    获取二维列表中任意一个元素
    :param map_given: 所给的区域（列表）
    :param pos_given: 所给的起始位置
    :param dir_given: 所给的方向
    :param count:步数（待获取元素的个数）
    :return: 要求的元素
    """
    res=[]
    for item in range(count):
        pos_given.x+=dir_given.x
        pos_given.y+=dir_given.y
        res.append(map_given[pos_given.x][pos_given.y])
    return res

# 使用类
list_given=[
    ['00','01','02','03'],
    ['10','11','12','13'],
    ['20','21','22','23'],
]
# 1.
pos01=Vector2(1,3)
dir01=pos01.left()
res_receive01=get_elements(list_given, pos01, dir01, 3)
print('res_receive01='+str(res_receive01))

# 2.
pos02=Vector2(2,2)
dir02=pos02.up()
res_receive02=get_elements(list_given, pos02, dir02, 2)
print('res_receive02='+str(res_receive02))

# 3.
pos03=Vector2(0,3)
dir03=pos03.down()
res_receive03=get_elements(list_given, pos03, dir03, 2)
print('res_receive03='+str(res_receive03))









