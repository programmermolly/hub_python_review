# 不用for循环，遍历以下字典：
# {'铁扇公主':101,'铁锤公主':102,'扳手王子':103}
dict_given={'铁扇公主':101,'铁锤公主':102,'扳手王子':103}
iterator=dict_given.__iter__()
while True:
    try:
        item=iterator.__next__()
        print(item)

    except StopIteration:
        print('获取完成！')
        break
