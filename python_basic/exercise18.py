# 对折纸
# 要求：一张纸的厚度为0.01毫米。请计算，对折多少次，厚度超过珠穆朗玛峰8848.43米

thickness = 0.01 / 1000
count = 0  # 计数器
while thickness <= 8848.43:
    thickness = thickness * 2
    count += 1

print(count)
