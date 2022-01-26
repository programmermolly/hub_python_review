# 要求：一个小球从100米的高度落下
# 每次弹回原高度的一半
# 小球的最小弹起高度为0.01米
# 计算一共弹起多少次
# 计算总共走了多少米

# 计算次数

height = 100
count = 0  # 计数器，记录小球弹起的次数
while True:
    height /= 2
    if height < 0.01:
        break
    count += 1

print('总共弹了%d次' % count)

# 计算走过的总路程

sum_value = 0
height = 100
for item in range(13):
    height = height / 2
    sum_value += height * 2
sum_value += 100
# 有来就有回，所以需要乘2
# 弹跳总路程+最初下落的100米
print('总共走了%d米' % int(sum_value))
