# 要求：在列表[54,25,12,60,75,87]中选出最大值

number_list=[54,25,12,60,75,87]
max_value=number_list[0]
for item in number_list:
    if item>max_value:
        max_value=item

print('最大值为：'+str(max_value))
