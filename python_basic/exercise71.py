# 打印函数的执行（被调用的）次数


count = 0


def fun_test(a, b):
    """
    :param a:
    :param b:
    :return: a和b的和
    """
    global count
    count += 1
    return a + b


# 调用函数
fun_test(1, 2)
fun_test(2, 3)
fun_test(4, 7)
print('count=%d' % count)
