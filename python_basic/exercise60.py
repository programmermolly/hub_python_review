# 列表全排列
# 概念：设有两个集合A和B，将两集合中元素两两组合，所得到的全部结果，称为全排列
# 现有两个列表
# ['香蕉','苹果','哈密瓜']
# ['可乐','牛奶']
# 打印其全排列

list_1 = ['香蕉', '苹果', '哈密瓜']
list_2 = ['可乐', '牛奶']
result = [fruit + drink for fruit in list_1 for drink in list_2]
print(result)
