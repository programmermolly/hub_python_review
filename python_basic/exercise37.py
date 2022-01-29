# 要求：在[9,25,12,8]删除大于10的数

numbers_list = [9, 25, 12, 8]

for item in range(len(numbers_list)-1,-1,-1):
    if numbers_list[item] > 10:
        numbers_list.remove(numbers_list[item])


# 验证
print(numbers_list)
