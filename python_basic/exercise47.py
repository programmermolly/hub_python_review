# 要求：允许多个用户输入多个爱好，（爱好）输入空字符串时表示（某用户）输入结束，姓名若为空则退出程序，打印所有爱好
dict_hobby = {}

while True:
    name = input('请输入您的姓名：')
    if name == '':
        break
    dict_hobby[name] = []
    while True:
        hobby = input('请输入您的爱好：')
        dict_hobby[name].append(hobby)
        if hobby == '':
            break
# 测试
# print(dict_hobby)
# 取数据
for key, value in dict_hobby.items():
    print('%s喜欢：' % key)
    for item in value:
        print(item)
