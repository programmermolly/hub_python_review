# 列表推导式练习
# 1.使用range()生成1-10之间的整数，并将它们的平方存入列表list01中
# 2.将list01中的所有奇数存入list02
# 3.将list01中的所有偶数存入list03
# 4.将list01中大于5的偶数加1后存入list04

list01 = [item ** 2 for item in range(1, 11)]
# 测试
print('列表1为：' + str(list01))
list02 = [item for item in list01 if item % 2 != 0]
# 测试
print('列表2为：' + str(list02))
list03 = [item for item in list01 if item % 2 == 0]
# 测试
print('列表3为：' + str(list03))
list04 = [item + 1 for item in list01 if item > 5 and item % 2 == 0]
# 测试
print('列表4为：' + str(list04))
