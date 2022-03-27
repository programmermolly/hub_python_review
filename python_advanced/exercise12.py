# 要求：定义my_zip()函数，实现zip()函数的功能

def my_zip(list_1, list_2):
    if len(list_1) < len(list_2):
        length = len(list_1)
    else:
        length = len(list_2)

    for index in range(length):
        yield list_1[index], list_2[index]


if __name__ == '__main__':
    list01 = ['孙悟空', '猪八戒', '唐僧', '沙僧']
    list02 = [101, 102, 103, 104]

    for item01, item02 in my_zip(list01, list02):
        print(item01, item02)
