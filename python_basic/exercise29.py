# 回文字符串
# 概念：倒序字符串和原字符串相同
usr_str=input('请输入字符串：')
if usr_str[::-1]==usr_str:
    print('该字符串是回文字符串')
else:
    print('该字符串不是回文字符串')