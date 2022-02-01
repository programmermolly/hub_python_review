# 根据日期计算天数
# 要求：在控制台中录入日期（月和日）计算这是一年的第几天（2月看作28天）
# 可选代码
# months_31=(1,3,5,7,8,10,12)
# months_30=(4,6,9,11)

day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
print('请输入日期')
month = int(input('请输入月：'))
day = int(input('请输入日：'))

days = 0
if month == 1:
    days = day
else:
    for num in range(month - 1):
        days += day_of_month[num]
    else:
        days += day
print("这是一年的第%d天" % days)
