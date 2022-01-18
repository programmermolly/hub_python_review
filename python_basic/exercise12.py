# 输入成绩，计算等级

score = int(input('请输入您的成绩：'))
if score > 100 or score < 0:
    print('输入有误，请重新输入！')
elif score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('不及格')
