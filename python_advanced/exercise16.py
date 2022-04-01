# 要求：使用内置函数获取元组([1,1,1],[2,2],[3,3,3,3])中最长的列表
tuple_given=([1,1,1],[2,2],[3,3,3,3])

print(max(tuple_given,key=lambda item:len(item)))
