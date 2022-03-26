# 要求：使用迭代器遍历以下容器
# ('铁扇公主','铁锤公主','扳手王子')
tuple_given = ('铁扇公主', '铁锤公主', '扳手王子')
iterator = tuple_given.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)

    except StopIteration:
        print('获取完成！')
        break
