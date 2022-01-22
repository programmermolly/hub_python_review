# 整数求和
# 计算：从1加到100
# 计算：1-100之间的所有偶数相加的和
# 计算：10-36之间的所有数相加的和

# 1.
# 存储累加和的变量，随着循环的进行，值逐渐增大，直到累加完毕，值为答案
sum1=0
for item_1 in range(101):
    sum1 += item_1
print('高斯求和为：' + str(sum1))

# 2.
sum2=0
for item_2 in range(1,101,2):
    sum2+=item_2
print('偶数和为：' + str(sum2))

# 3.
sum3=0
for item_3 in range(10, 37):
    sum3+=item_3
print('10到36所有数累加后为：' + str(sum3))
