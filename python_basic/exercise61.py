# 定义函数
# 将下列代码作为函数体定义一个函数，并调用它
# for r in range(3):
#     for c in range(4):
#         print('*',end=" ")
#     print()

def star_printing():
    """
    此函数用来打印“*”
    缺点：适用性不高
        如需类似功能，还需重新定义函数
        所以，应为函数设置参数
        使其可打印任意尺寸的矩形
    """
    for r in range(3):
        for c in range(4):
            print('*', end=" ")
        print()


# 调用函数
star_printing()
