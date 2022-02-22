# 要求：
# 1.创建学生类
#   数据：姓名、年龄、成绩、性别
#   行为：在控制台中输出个人信息
# 2.创建对象，调用方法
#   在控制台中录入学生信息，输入空字符串停止，
#   调用方法输出录入的信息
#  3.其他要求
#     输出格式为：xxx的年龄是xx，性别是xx，成绩为xx

class Student:
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def info_output(self):
        print('%s的年龄是%s，性别是%s，成绩为%s分' % (self.name, self.age, self.gender, self.score))


# 用户输入学生信息及创建对象
list_info = []
while True:
    stu_name = input('请输入学生姓名：')
    if stu_name == '':
        break
    stu_age = input('请输入学生年龄：')
    stu_gender = input('请输入学生性别：')
    stu_score = input('请输入学生成绩：')

    # 创建对象
    student = Student(stu_name, stu_age, stu_gender, stu_score)
    list_info.append(student)

# 调用方法
for item in list_info:
    item.info_output()
