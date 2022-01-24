# 输入一个字符串，打印每个字符的编码值
# 遍历字符串中的每个字符，打印其编码值
usr_str = input('请输入字符串：')

for item in usr_str:
    code_str = ord(item)

    print(code_str)
