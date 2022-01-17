# 判断是闰年还是平年

year = int(input('请输入年份：'))

res = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

if res == True:
    print('是闰年')
