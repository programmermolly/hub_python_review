# 计算找零金额（用选择语句进行扩展）

price = int(input('请输入商品单价：'))
number = int(input('请输入商品数量：'))
money = int(input('请输入所付金额：'))

change = money - price * number
more_money = price * number - money
if money >= price * number:
    print('找零金额为：' + str(change))
else:
    print('您还应该再付：' + str(more_money))
