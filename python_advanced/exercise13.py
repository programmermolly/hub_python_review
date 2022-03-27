# 要求：1.获取列表中所有字符串
# 要求：2.获取列表中所有小数
# list01=[3,'54',True,6,76,1.6,False,3.5]

list01=[3,'54',True,6,76,1.6,False,3.5]

generator1=(item for item in list01 if type(item)==str)

for item in generator1:
    print(item)

generator2=(item for item in list01 if type(item)==float)

for item in generator2:
    print(item)