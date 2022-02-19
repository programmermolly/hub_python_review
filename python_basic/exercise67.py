# 定义一个函数，判断列表中是否有相同元素

def repeating_element_judgment(list_numbers):
    """
    判断列表中是否有重复元素
    """
    flag = True
    for i in range(5):
        for n in range(i + 1, 6):
            if list_numbers[i] == list_numbers[n]:
                pass

    if flag == True:
        return '有重复元素！'
    else:
        return '正常！'
# 测试函数
li=[3,80,45,80,7,1]
print(repeating_element_judgment(li))
