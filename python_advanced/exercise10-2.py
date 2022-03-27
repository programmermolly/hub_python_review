# 要求：从列表[4,5,566,7,8,10]中获取所有偶数

list_given = [4, 5, 566, 7, 8, 10]


def get_even_number():
    index = 0
    while True:
        if index == 6:
            break
        if list_given[index] % 2 == 0:
            yield list_given[index]
        index += 1


if __name__ == '__main__':

    for item in get_even_number():
        print(item)
