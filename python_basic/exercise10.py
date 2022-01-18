# 简易计算器（仅含加、减、乘、除功能）

number_1 = int(input('请输入第一个数字：'))
number_2 = int(input('请输入第二个数字：'))
op = input('请输入运算符：')

res = None
if op == '+':
    res = number_1 + number_2
elif op == '-':
    res = number_1 - number_2
elif op == '×':
    res = number_1 * number_2
elif op == '÷':
    res = number_1 / number_2
else:
    print('运算符输入有误！')

if res is not None:
    print(str(number_1) + op + str(number_2) + '=' + str(res))
else:
    pass
