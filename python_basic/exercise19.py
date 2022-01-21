# 猜数字游戏 v1.0
# 要求:计算机随机产生一个1-100之间的随机数，让用户去猜，直到猜对为止。
# 每猜一次，程序需要提示用户：大了/小了/猜对了，你真棒！
# 产生随机数，可以用下列代码
# import random
# random_number=random.randint(1,100)

import random

random_number = random.randint(1, 100)
# 接收用户输入
while True:
    usr_input = input('请输入你猜得整数，按q退出：')
    if usr_input == 'q':
        break
    elif int(usr_input) > random_number:
        print('大了')
    elif int(usr_input) < random_number:
        print('小了')
    else:
        print('猜对了，你真棒！')
        break
