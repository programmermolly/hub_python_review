# 猜数字游戏（加强版）v2.0
# 要求:计算机随机产生一个1-100之间的随机数，让用户去猜，只能猜3次。
# 每猜一次，程序需要提示用户：大了/小了/猜对了，你真棒！
# 若猜对，退出程序，游戏结束。
# 若三次都未猜对，则提示用户：“失败”
# 产生随机数，可以用下列代码
# import random
# random_number=random.randint(1,100)

import random

random_number = random.randint(1, 100)
# 接收用户输入
count = 0  # 计数器
while count < 3:
    count += 1
    usr_input = input('请输入你猜得整数，按q退出：')

    if int(usr_input) > random_number:
        print('大了')
    elif int(usr_input) < random_number:
        print('小了')
    else:
        print('猜对了，你真棒！')
        break
# 三次都未猜对，游戏失败
else:
    print('失败')
