# 要求：有如下列表
# list01=[43,4,5,5,6,7,87]
# 完成下列各题
# 1.查找所有偶数
# 2.查找所有大于10的数
# 3.查找10-50之间的数
# 先用生成器函数完成3道题
# 然后，按如下步骤改为函数式编程
#   （1）将函数当中变化的部分放到另外3个函数中
#   （2）将不变的部分单独放在一个函数中
# 最后进行测试
list01 = [43, 4, 5, 5, 6, 7, 87]


def find(func):
    for item in list01:
        if func(item):
            yield item


def condition01(item):
    return item % 2 == 0


def condition02(item):
    return item > 10


def condition03(item):
    return 10 <= item <= 50

