# 要求：存储各个城市的景区与美食，并打印在控制台中（无需录入）
# 考点：数据结构的选择
"""
北京：
景区：故宫、天坛、天安门
美食：烤鸭、炸酱面、豆汁、卤煮
四川：
景区：九寨沟、峨嵋山、春熙路
美食：火锅、串串香、兔头
"""
dict_cities = {'北京': {'景区': ['故宫', '天坛', '天安门'], '美食': ['烤鸭', '炸酱面', '豆汁', '卤煮']},
               '四川': {'景区': ['九寨沟', '峨嵋山', '春熙路'], '美食': ['火锅', '串串香', '兔头']}

               }
# 测试
# print(dict_cities)
for city, info in dict_cities.items():
    print('%s:'%city)
    for category, content in info.items():
        print('%s:'%category,end='')
        for item in content:
            print(item,end=' ')
