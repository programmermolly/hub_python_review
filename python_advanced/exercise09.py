# 编写MyRange类，使其对象实现如下功能:
# for item in range(10):
#    print(item)
# 即生成0-9 10个数，并可以用for循环获取

class MyRange:
    def __init__(self, end):
        self.x = 0
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self.end)


class MyRangeIterator:
    def __init__(self, end_value):
        self.x = 0
        self.end_value = end_value

    def __next__(self):
        if self.x == self.end_value:
            raise StopIteration
        temp = self.x
        self.x += 1
        return temp


if __name__ == '__main__':
    iterator = MyRange(10).__iter__()
    while True:
        try:
            item = iterator.__next__()
        except StopIteration:
            break
        print(item)
