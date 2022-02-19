# 要求：定义一个函数，其可以根据成绩计算等级
# 参考代码

# score = int(input('请输入您的成绩：'))
# if score > 100 or score < 0:
#     print('输入有误，请重新输入！')
# elif score >= 90:
#     print('优秀')
# elif score >= 80:
#     print('良好')
# elif score >= 60:
#     print('及格')
# else:
#     print('不及格')

def rank_judgment(score):
    """
    判断等级
    """

    if score > 100 or score < 0:
        return '输入有误，请重新输入！'
    elif score >= 90:
        return '优秀'
    elif score >= 80:
        return '良好'
    elif score >= 60:
        return '及格'
    else:
        return '不及格'


# 测试函数
sc = int(input('请输入您的成绩：'))
print(rank_judgment(sc))
