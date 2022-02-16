# 编写打印二维列表中的元素的函数
# 概念：二维列表指含有子列表的列表
# 如：
# [
# [1,2,3,4],
# [5,6,7,8],
# ]

def matrix_printing(mat):
    for item in mat:
        for n in item:
            print(n)


# 调用函数
test_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
]
matrix_printing(test_list)
