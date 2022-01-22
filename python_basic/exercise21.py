# 录入成绩，判断等级
# 要求：用户录入成绩，若有三次录入错误（录入的分数不在0-100范围内），则提示“错误过多，程序退出”。
# 注：如果用户录入空字符串则退出程序
count = 0  # 计数器
while count < 3:
    score = input('请输入您的成绩：')
    if score == '':
        break

    if int(score) > 100 or int(score) < 0:
        print('输入有误，请重新输入！')
        count += 1
    elif int(score) >= 90:
        print('优秀')
    elif int(score) >= 80:
        print('良好')
    elif int(score) >= 60:
        print('及格')
    else:
        print('不及格')
else:
    print('错误过多，程序退出')
