# 计算加速度
# 加速度=（距离-初速度×时间）×2/时间的平方

in_speed=int(input('请输入初速度：'))
distance=int(input('请输入距离：'))
time=int(input('请输入时间：'))

acce_speed=(distance-in_speed*time)*2/time**2

print('加速度为：'+str(acce_speed))

