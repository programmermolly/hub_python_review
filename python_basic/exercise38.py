# 要求：在控制台中输入字符串，输入空字符串表示输入结束
# 将所有输入的字符串拼接为一个字符串并打印

list_temp = []
while True:
    usr_str = input('请输入字符串：')
    if usr_str != '':
        list_temp.append(usr_str)
    else:
        break

new_str = ' '.join(list_temp)
print(new_str)
# 验证
# print(type(new_str))
