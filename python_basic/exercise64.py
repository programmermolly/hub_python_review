# 练习：定义一个函数，计算四位数的数字和
# 并测试

# number=int(input('请输入一个四位整数：'))
#
# units=number%10
# tens=number//10%10
# hundreds=number//100%10
# thousands=number//1000
#
# res=units+tens+hundreds+thousands
# print('四位数字的和为：'+str(res))

def calculate_numbers_addition(number):
    """
    此函数用来计算四位数的数字和
    """
    units = number % 10
    tens = number // 10 % 10
    hundreds = number // 100 % 10
    thousands = number // 1000

    res = units + tens + hundreds + thousands
    return res


# 测试函数
usr_number = int(input('请输入一个四位数：'))
print(calculate_numbers_addition(usr_number))
