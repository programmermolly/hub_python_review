# 要求：
# 在控制台中录入学生信息（姓名、年龄、成绩、性别）当姓名为空字符串时结束输入，打印所有信息
dict_info={}
tuple_info=()
while True:
    name=input('请输入学生姓名：')
    if name=='':
        break
    age=input('请输入学生年龄：')
    score=input('请输入学生成绩：')
    sex=input('请输入学生性别：')
    dict_info[name]=(age,score,sex)
# 测试
print(dict_info)
