# 转置列表
# 要求：将如下列表转置
"""[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
    """
list_known = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
new_list = []
# line1=[list_known[n][0] for n in range(4)]
# print(line1)
# line2=[list_known[n][1] for n in range(4)]
# print(line2)

# 法一：
line1 = [list_known[n][0] for n in range(4)]
# print(line1)
line2 = [list_known[n][1] for n in range(4)]
# print(line2)
line3 = [list_known[n][2] for n in range(4)]
line4 = [list_known[n][3] for n in range(4)]
new_list.append(line1)
new_list.append(line2)
new_list.append(line3)
print(new_list)

# 法二：
result = []
for m in range(4):
    line = [list_known[n][m] for n in range(4)]
    result.append(line)
print(result)
