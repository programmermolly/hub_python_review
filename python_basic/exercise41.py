import random

lottery = []  # 存储号码
# 6个红球

number_1 = random.randint(1, 33)
number_2 = random.randint(1, 33)
number_3 = random.randint(1, 33)
number_4 = random.randint(1, 33)
number_5 = random.randint(1, 33)
number_6 = random.randint(1, 33)
# 1个蓝球

number_7 = random.randint(1, 16)

# 生成彩票
lottery.append(number_1)
lottery.append(number_2)
lottery.append(number_3)
lottery.append(number_4)
lottery.append(number_5)
lottery.append(number_6)
lottery.append(number_7)

# 打印彩票
if number_1 != number_2 != number_3 != number_4 != number_5 != number_6:
    print('示例彩票：' + str(lottery))
else:
    print('示例彩票有误，不可打印！请重新打印或直接购买！')
purchase_lottery = []

# 购买彩票
for item in range(6):
    while True:
        usr_number_1 = int(input('请输入第%d个红球号码：' % (item + 1)))

        if usr_number_1 > 33:
            print('号码不在范围内！')

        elif usr_number_1 in purchase_lottery:
            print('号码已经存在！')

        else:
            purchase_lottery.append(usr_number_1)
            break

while True:
    usr_number_2 = int(input('请输入蓝球号码：'))
    if usr_number_2 > 16:
        print('号码不在范围内！')
    else:
        purchase_lottery.append(usr_number_2)
        break

print('购买成功！欢迎下次光临！')
print(purchase_lottery)
