# 加法练习器
# 要求：1.随机出3道题（10以内加法），让用户作答，作对得10分
#      2.做错不得分，最后计算总分

import random

score = 0  # 记分器

for item in range(3):
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    usr_number = int(input(str(num_1) + '+' + str(num_2) + '=' + '?' + ' ' + '请输入'+' '))
    if usr_number == num_1 + num_2:
        score += 10
    else:
        pass

print('总得分是：' + str(score))
