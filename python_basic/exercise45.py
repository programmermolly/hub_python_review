# 练习：在控制台中录入商品信息（包括品名和单价）
# 输入空字符串代表输入结束
# 逐行打印所有信息
info = {}
while True:
    usr_name = input('请输入商品名称：')
    if usr_name == '':
        break
    usr_price = input('请输入商品单价：')

    info[usr_name] = usr_price

for item in info.items():
    print(item)
