# 要求：不使用python自带的函数完成此题
# 在控制台中录入5个整数，打印最大数
numbers = []
for item in range(5):
    input_numbers = int(input('请输入第%d个整数：' % (item + 1)))
    numbers.append(input_numbers)

max_value = numbers[0]
for item in range(4):
    if item > max_value:
        max_value = item

print('5个数的最大值为：' + str(max_value))
