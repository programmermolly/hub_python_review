# 要求：1.获取攻击比例大于6的所有技能，必须用生成器完成此题
#      2.获取持续时间在4-11之间的所有技能，必须用生成器完成此题
#      3.获取编号为102的技能，必须用生成器完成此题
#      4.获取技能名称大于4个字，且持续时间小于6的所有技能，必须用生成器完成此题

# 技能列表及属性如下
"""
class SkillData:
    def __init__(self,id,name,atk_ratio,duration):
        self.id=id
        self.name=name
        self.atk_ratio=atk_ratio
        self.duration=duration

list_skill=[
    SkillData(101,'乾坤大挪移',5,10),
    SkillData(102,'降龙十八掌',8,5),
    SkillData(103,'葵花宝典',10,2),
]
"""


class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration


list_skill = [
    SkillData(101, '乾坤大挪移', 5, 10),
    SkillData(102, '降龙十八掌', 8, 5),
    SkillData(103, '葵花宝典', 10, 2),
]

generator1 = (list_skill[index] for index in range(3) if list_skill[index].atk_ratio > 6)
print('1.')
for item in generator1:
    print(item.name)
print()
print('2.')
generator2=(list_skill[index] for index in range(3) if 4<=list_skill[index].duration<=11)
for item in generator2:
    print(item.name)
print()

print('3.')
generator3=(list_skill[index] for index in range(3) if list_skill[index].id==102)
for item in generator3:
    print(item.name)
print()

print('4.')
generator4=(list_skill[index] for index in range(3) if len(list_skill[index].name)>4 and list_skill[index].duration<6)
for item in generator4:
    print(item.name)
