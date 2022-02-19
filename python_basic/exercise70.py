# 定义一个函数，其可转置矩阵（方阵）

def matrix_transpose(list_known):
    for i in range(1,len(list_known)):
        for j in range(i,len(list_known)):
            list_known[j][i-1],list_known[i-1][j]=list_known[i-1][j],list_known[j][i-1]

    return list_known

# 测试函数
list_test=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
print(matrix_transpose(list_test))
# 测试
# print(list_test)






