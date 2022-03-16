"""
思路总结：
1.列表就是一种顺序存储结构，但是功能太多
2.所以，我们封装列表，写自己的操作方法
"""


# 3.自定义异常：栈错误

# 顺序栈
# 自定义异常


class StackError(Exception):
    pass


class SStack:
    def __init__(self):
        # 栈的存储空间
        # 规定：将列表的末端作为栈顶
        self.__elements = []

    def is_empty(self):
        """
        判断是否为空栈
        """
        return self.__elements == []

    # 入栈
    def push(self, value):
        self.__elements.append(value)

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError('Stack is empty!')
        return self.__elements.pop()

    # 查看栈顶元素
    def top(self):
        return self.__elements[-1]



