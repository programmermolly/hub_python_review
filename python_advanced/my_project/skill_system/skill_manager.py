import common.double_list_helper as dlh
import main
from common import double_list_helper


class SkillManager_test:
    def __init__(self, attack, hp):
        self.attack = attack
        self.hp = hp

    @staticmethod
    def attack_test():
        print('攻击！')

    def hp_test(self):
        print('掉了%d血' % self.hp)


my_test = double_list_helper.Test(2, 5)
my_test.test1()
dlh.Test.test2()
main.sd.SkillManager.hp()
