from skill_system import skill_manager


class SkillManager:
    def __init__(self, attack, hp):
        self.attack = attack
        self.hp = hp

    @staticmethod
    def attack():
        print('攻击！')

    def hp(self):
        print('掉了%d血' % self.hp)

    @staticmethod
    def developed():
        print('够了！')


sm = skill_manager.SkillManager_test(100, 50)
sm.hp()
sm.attack()
