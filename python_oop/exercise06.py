# 要求：有如下列表：
# list01=[
#         Student('赵敏',28,100,'女'),
#         Student('苏大强',68,62,'男'),
#         Student('明玉',30,95,'女'),
#         Student('无忌',29,70,'男'),
#         Student('张三丰',130,96,'男')
# ]
# 将所有学生的成绩归零
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


def score_to_zero():
    for item in list01:
        item.score = 0


# 调用方法
score_to_zero()
for item in list01:
    print(item.score)
