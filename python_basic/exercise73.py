# 要求：定义一个函数，计算若干个数的和(数值相加)

def numbers_addition(*args):
    return sum(args)


# 测试函数
print(numbers_addition(1, 2, 3, 4, 5))
