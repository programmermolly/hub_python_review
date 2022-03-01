# 要求：定义“敌人”类：
# 数据：姓名、生命、初始攻击力、防御力
# 行为：打印自身信息
# 1.创建至少4个敌人，存到列表中
# 2.查找名叫“灭霸”的敌人
# 3.查找死亡的敌人
# 4.计算平均攻击力
# 5.删除防御力小于10的敌人
# 6.将所有对象的攻击力增加50

class Enemy:
    def __init__(self, name, life, ini_attack, defence):
        self.name = name
        self.life = life
        self.ini_attack = ini_attack
        self.defence = defence

    def info_output(self):
        print('姓名：%s \n 血量：%d \n 攻击：%d \n 防御：%d' % (self.name, self.life, self.ini_attack, self.defence))

    @staticmethod
    def find_enemy():
        for item in list_enemies:
            if item.name == '灭霸':
                item.info_output()

    @staticmethod
    def find_dead_enemy():
        for item in list_enemies:
            if item.life == 0:
                print('死亡的敌人是：%s' % item.name)

    @staticmethod
    def average_attack():
        return sum(attack_enemies) / len(attack_enemies)

    @staticmethod
    def delete_enemies():
        for item in list_enemies:
            if item.defence < 10:
                list_enemies.remove(item)

    @staticmethod
    def add_attack():
        for item in list_enemies:
            item.ini_attack += 50


# 创建对象
ene1 = Enemy('灭霸', 100, 100, 100)
ene2 = Enemy('刘邦', 200, 85, 100)
ene3 = Enemy('赵高', 0, 5, 8)
ene4 = Enemy('项羽', 300, 400, 500)
ene5 = Enemy('小乔', 60, 40, 80)

list_enemies = [ene1, ene2, ene3, ene4, ene5]
attack_enemies = [
    ene1.ini_attack,
    ene2.ini_attack,
    ene3.ini_attack,
    ene4.ini_attack,
    ene5.ini_attack,
]

# 使用类
Enemy.find_enemy()
print()
Enemy.find_dead_enemy()
print()
res = Enemy.average_attack()
print(res)
print()
Enemy.add_attack()
for item in list_enemies:
    item.info_output()
print()
Enemy.delete_enemies()
for item in list_enemies:
    item.info_output()
