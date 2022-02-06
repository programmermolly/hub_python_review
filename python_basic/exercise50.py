# 要求：计算一个字符串中的字符及其出现的次数
# 例如：abcdabccaab
# 统计：a出现？次，b出现？次
dict_str = {}

my_str = 'abcdabccaab'
for item in my_str:

    if item in dict_str:
        dict_str[item] += 1

    else:
        dict_str[item] = 1

print(dict_str)

