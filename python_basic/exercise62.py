# 定义一个函数，打印列表中的元素，每个元素占一行

def printing_lists(li):
    """
    此函数用于打印列表中的元素

    每行一个元素
    """
    for item in li:
        print(item)


# 调用函数
test_list = [1, 2, 3, 4, 5]  # 这叫测试用例，即测试函数功能用的实例
printing_lists(test_list)
