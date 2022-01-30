# 英文单词翻转
# 要求：将“How are you ?”变成“？you are How ”

former_str = 'How are you ?'
list_required = former_str.split(' ')
# print(list_required)
temp_list = list_required[::-1]
# print(temp_list)
statement = ' '.join(temp_list)
print(statement)
# print(type(statement))
