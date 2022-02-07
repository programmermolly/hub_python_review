# 要求：[赵敏 周芷若 无忌]
# 变化为：{赵敏：2,周芷若：3 无忌：2}
list_person=['赵敏','周芷若','无忌']
dict_person={item:len(item) for item in list_person}

print(dict_person)