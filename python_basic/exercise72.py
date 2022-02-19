# 要求：定义一个函数，根据小时，分钟，秒，计算总秒数
# 用户可以自由选择根据小时、分钟、秒中一种或几种计算总秒数

def calculate_seconds(hours=0, minutes=0, seconds=0):
    """
    得到总秒数
    """
    return hours * 3600 + minutes * 60 + seconds


# 测试函数
print(calculate_seconds(3, 2))
