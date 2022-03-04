# 要求：定义“敌人”类，数据有姓名，攻击力，血量
# 其中：
# 1.攻击力的范围是10-50
# 2.血量的范围是100-200
# 3.除姓名外，其余数据需向用户隐藏，提供读取和修改的方法。
# 本题需用property()方法进行私有化

class Enemy:
    def __init__(self, name, attack, life):
        self.name = name
        self.attack=attack
        self.life=life
    def get_attack(self):
        return self.__attack
    def set_attack(self, usr_setting):
        if 10 <= usr_setting <= 50:
            self.__attack = usr_setting
        else:
            raise ValueError('攻击力不在范围内！')

    def get_life(self):
        return self.__life

    def set_life(self, usr_setting):
        if 100 <= usr_setting <= 500:
            self.__life = usr_setting
        else:
            raise ValueError ('血量不在范围内！')

    attack=property(get_attack,set_attack)
    life=property(get_life,set_life)
# 使用类
ene01 = Enemy('刘邦', 20, 100)
print(ene01.__dict__)

print(ene01.get_attack())
ene01.attack=5
ene01.attack=30
print(ene01.get_attack())
print(ene01.get_life())
ene01.life=600
ene01.life=500
print(ene01.get_life())
