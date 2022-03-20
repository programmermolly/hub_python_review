class Vector2:
    """
    辅助获取二维列表元素的类
    """

    def __init__(self, x, y):
        """
        初始化类
        :param x: 外索引
        :param y: 内索引
        """
        self.x = x
        self.y = y

    # 表示方向
    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)


def get_elements(map_given, pos_given, dir_given, count):
    """
    获取二维列表中任意一个元素
    :param map_given: 所给的区域（列表）
    :param pos_given: 所给的起始位置
    :param dir_given: 所给的方向
    :param count:步数（待获取元素的个数）
    :return: 要求的元素
    """
    res = []
    for item in range(count):
        pos_given.x += dir_given.x
        pos_given.y += dir_given.y
        res.append(map_given[pos_given.x][pos_given.y])
    return res

