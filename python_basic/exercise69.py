# 练习：定义可以升序排列列表元素的函数
def ascending_arrangement(list_required):
    for i in range(len(list_required) - 1):
        for j in range(i + 1, len(list_required)):
            if list_required[i] > list_required[j]:
                list_required[i], list_required[j] = list_required[j], list_required[i]
            else:
                pass
    return list_required


# 测试函数
li = [43, 4, 5, 6, 7]
print(ascending_arrangement(li))
