# 要求：在控制台中录入字符串，输入空字符串表示输入结束
# 打印所有不重复的文字
set_str= set()
while True:
    str_input=input('请输入文字：')
    if str_input=='':
        break
    set_str.add(str_input)

# 测试
# print(set_str)
for character in set_str:
    print(character)
