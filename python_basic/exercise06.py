# 计算四位数的数字和

number=int(input('请输入一个四位整数：'))

units=number%10
tens=number//10%10
hundreds=number//100%10
thousands=number//1000

res=units+tens+hundreds+thousands
print('四位数字的和为：'+str(res))
