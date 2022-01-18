# 找出最大数字

num_1 = input('请输入第一个数字：')
num_2 = input('请输入第二个数字：')
num_3 = input('请输入第三个数字：')
num_4 = input('请输入第四个数字：')
max_number = int(num_1)
if int(num_2) <= max_number:
    pass
else:
    max_number = int(num_2)
if int(num_3) > max_number:
    max_number = int(num_3)
if int(num_4) > max_number:
    max_number = num_4

print('最大值为：' + str(max_number))
