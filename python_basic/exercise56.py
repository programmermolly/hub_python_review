# 列表去重
# 判断列表[3,80,45,80,7,1]中是否有重复元素
# 思路：所有元素两两比较，若发现相同元素，则输出“有重复元素”，否则输出“正常”

list_numbers=[3,80,45,80,7,1]
flag=True
for i in range(5):
    for n in range(i+1,6):
        if list_numbers[i]==list_numbers[n]:
            pass

if flag==True:
    print('有重复元素！')
else:
    print('正常！')



