# 要求：有如下列表：
# list01=[
#         Student('赵敏',28,100,'女'),
#         Student('苏大强',68,62,'男'),
#         Student('明玉',30,95,'女'),
#         Student('无忌',29,70,'男'),
#         Student('张三丰',130,96,'男')
# ]
# 统计不小于30岁学生的数量

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
list_temp = []


def calculate_old_student():
    for item in list01:
        if item.age >= 30:
            list_temp.append(item)
    return len(list_temp)


# 调用方法
print(calculate_old_student(list01))
