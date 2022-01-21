# 打印中间值

num_1 = int(input('请输入开始值：'))
num_2 = int(input('请输入结束值：'))
count = 0  # 计数器
num = num_1
while count < num_2 - num_1 - 1:
    num += 1
    print(num)
    count += 1
