# 2048游戏核心算法
# 定义将0元素移至末尾的函数


def move_element(list_numbers):
    """
    将0元素移动到列表末尾
    """
    for i in range(len(list_numbers)):
        for j in range(i, len(list_numbers)):
            if list_numbers[i] == 0:
                list_numbers[i], list_numbers[j] = list_numbers[j], list_numbers[i]
            else:
                pass


# 将非零的相同数字合并（相加）
def add_same_numbers(list_numbers):
    """
    将相同的两个数字（非零）相加
    """
    move_element(list_numbers)
    for i in range(len(list_numbers) - 1):
        if list_numbers[i] == list_numbers[i + 1] and list_numbers[i]:
            list_numbers[i] += list_numbers[i + 1]
            del list_numbers[i + 1]
            list_numbers.append(0)


# 将地图向左移动
map_2048 = [
    [2, 0, 0, 2],
    [4, 4, 2, 2],
    [2, 4, 0, 4],
    [0, 0, 2, 2]
]


def move_left(list_map):
    for item in list_map:
        add_same_numbers(item)


def move_right(list_map):
    """
    地图向右移动
    """
    for item in list_map:
        global row
        row = item[::-1]
        add_same_numbers(row)
        item[::-1] = row


def move_up(list_map):
    matrix_transpose(list_map)
    move_left(list_map)
    matrix_transpose(list_map)


def move_down(list_map):
    matrix_transpose(list_map)
    move_right(list_map)
    matrix_transpose(list_map)


def matrix_transpose(list_known):
    for i in range(1, len(list_known)):
        for j in range(i, len(list_known)):
            list_known[j][i - 1], list_known[i - 1][j] = list_known[i - 1][j], list_known[j][i - 1]

    return list_known
