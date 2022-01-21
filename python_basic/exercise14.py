# 为变量赋值（用条件表达式）
# 方法1：传统方法
# user_input=int(input('请输入一个整数：'))
# if user_input%2==0:
#     state='偶数'
# else:
#     state='奇数'
#
# print(state)
# 方法2：条件表达式法
user_input = int(input('请输入一个整数：'))
state = '偶数' if user_input % 2 == 0 else '奇数'
print(state)
