# 要求：[赵敏 周芷若 无忌] [101,102,103]
# 变化为：{无忌：101 赵敏：102,周芷若：103 }

list_person=['无忌','赵敏','周芷若']
list_num=[101,102,103]
dict_person={list_person[n]:list_num[n] for n in range(3) }
print(dict_person)