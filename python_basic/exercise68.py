# 要求：定义一个函数，判断某个月份有多少天，考虑闰年
# 参考代码：不考虑闰年的情况
# month = input('请输入月份：')
# if int(month) in (1, 3, 5, 7, 8, 10, 12):
#     print('该月有31天')
# if month == '2':
#     print('该月有28天')
# if int(month) in (4, 6, 9, 11):
#     print('该月有30天')
# if int(month) > 12:
#     print('输入有误！')
# month = input('请输入月份：')
# if int(month) in (1, 3, 5, 7, 8, 10, 12):
#     print('该月有31天')
# if month == '2':
#     print('该月有28天')
# if int(month) in (4, 6, 9, 11):
#     print('该月有30天')
# if int(month) > 12:
#     print('输入有误！')

def day_of_month(y, m):
    """
    提供月份的天数
    """
    if y % 4 != 0 and y % 100 != 0 and y % 400 != 0:
        if int(m) in (1, 3, 5, 7, 8, 10, 12):
            return '该月有31天'
        if m == '2':
            return '该月有28天'
        if int(m) in (4, 6, 9, 11):
            return '该月有30天'
        if int(m) > 12:
            return '输入有误！'
    else:
        if int(m) in (1, 3, 5, 7, 8, 10, 12):
            return '该月有31天'
        if int(m) == 2:
            return '该月有29天'
        if int(m) in (4, 6, 9, 11):
            return '该月有30天'
        if int(m) > 12:
            return '输入有误！'


# 调用函数
print(day_of_month(2000, 2))
