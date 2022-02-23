# 要求：有如下列表：
# list01=[
#         Student('赵敏',28,100,'女'),
#         Student('苏大强',68,62,'男'),
#         Student('明玉',30,95,'女'),
#         Student('无忌',29,70,'男'),
#         Student('张三丰',130,96,'男')
# ]
# 定义一个查找对象的函数，查找列表中所有女同学
# 将姓名和年龄打印在控制台中
class Student:
    def __init__(self, name, age, score, gender):
        self.name = name
        self.age = age
        self.score = score
        self.gender = gender


list01 = [
    Student('赵敏', 28, 100, '女'),
    Student('苏大强', 68, 62, '男'),
    Student('明玉', 30, 95, '女'),
    Student('无忌', 29, 70, '男'),
    Student('张三丰', 130, 96, '男')
]


def find_female_student(list_known):
    for item in list_known:
        if item.gender == '女':
            print(item.name, item.age)


# 调用方法
find_female_student(list01)
