# 要求：用户输入一个年份，如果是闰年，day=29，否则，day=28
# 用条件表达式
user_input = int(input('请输入一个年份：'))
day = 29 if user_input % 4 == 0 and user_input % 100 != 0 or user_input % 400 == 0 else 28
print(day)
