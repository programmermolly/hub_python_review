# 字符串索引和切片
# 在控制台中获取一个字符串
# 1.打印第一个字符
# 2.打印最后一个字符
# 3.打印倒数第三个字符
# 4.打印前两个字符
# 5.倒序打印字符串
# 6.如果字符串长度为奇数，打印中间字符

# 字符串长度为偶数

usr_str = input('请输入一个字符串：')
# 1.用索引，取出单个字符
print('第一个字符为：%s' % (usr_str[0]))
# 2.用索引
print('最后一个字符为：%s' % (usr_str[-1]))
# 3.用索引
print('倒数第三个字符为：%s' % (usr_str[-3]))
# 4.用切片，取出连续的多个字符
print('前两个字符为：%s' % (usr_str[:2]))
# 5.用反向切片，获取原字符串
print('倒序打印的结果是：' + usr_str[::-1])
