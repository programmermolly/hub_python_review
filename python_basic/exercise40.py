# 找出[1,45,9,13,179]中最小的数字（不使用自带函数）
numbers_list = [1, 45, 9, 13, 179]
min_value = numbers_list[0]
for n in numbers_list:
    if n < min_value:
        min_value = n
print('最小值为：' + str(min_value))
