# 要求：在控制台中录入所有学生姓名
# 输入空字符串表示结束
# 如果姓名与已有姓名重复，就向用户发出提示，并不再将其填入列表
# 倒序打印所有姓名

names = []
while True:
    name = input('请输入学生姓名，按enter键结束（每次只能输入一个姓名）：')
    if name == '':
        break
    if name not in names:
        names.append(name)
    else:
        print('姓名已存在，请重新输入或结束输入！')

for i in range((len(names) - 1), -1, -1):
    print(names[i])
