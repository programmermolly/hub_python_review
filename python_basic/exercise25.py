# 累加10-50之间个位不是2、5、9的整数(包括10和50)
# 依次相加 1+2+3+4...
sum_value = 0  # 存储和
for item in range(10, 51):
    if item % 10 != 2 or item % 10 != 5 or item % 10 != 9:
        sum_value += item
print('和为：' + str(sum_value))
