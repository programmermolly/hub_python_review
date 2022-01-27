# 生成并操作列表
# 要求：1.生成一个空列表
#      2.通过控制台录入你喜欢的西游人物
#      3.输入空字符串表示录入结束
#      4.打印所有人物

characters = []

while True:
    favourite_character = input('请输入你喜欢的西游人物，按enter键结束(每次只能输入一个)：')
    characters.append(favourite_character)
    if favourite_character == '':
        break

for item in characters:
    print(item)
