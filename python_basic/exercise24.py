# 判断素数
# 方法：从1开始依次判断每个数字是否为其因数（排除法）

number = int(input('请输入一个数：'))
flag = True
for item in range(2, number):
    if number % item:
        pass
    else:
        flag = False
        break
if flag:
    print('是素数')
else:
    print('不是素数')
