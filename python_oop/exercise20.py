# 要求：创建enemy类的对象，并将其打印在控制台上（以字符串形式，格式自定）
# 克隆上面的对象

class Enemy:
    def __init__(self, name, hp, atk, defence):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence

    def __str__(self):
        return ' 姓名：%s\n 血量：%s\n 攻击力：%s\n 防御力：%s' % (self.name, self.hp, self.atk, self.defence)

    def __repr__(self):
        return 'Enemy("%s",%s,%s,%s)' % (self.name, self.hp, self.atk, self.defence)


ene = Enemy('mb', 100, 2000, 30000)
print(str(ene))

# 克隆对象
ene_copy = eval(repr(ene))
print(type(ene_copy))
