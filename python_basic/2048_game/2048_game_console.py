# 打印棋盘
import random


class Game():
    def __init__(self):
        self.score = 0
        self.list = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        # 白板 存储坐标
        self.whiteBoard = []

    def restart(self):
        self.list = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        while True:
            t1 = [random.randrange(len(self.list)), random.randrange(len(self.list[0]))]
            t2 = [random.randrange(len(self.list)), random.randrange(len(self.list[0]))]
            if t1 != t2:
                break
        self.list[t1[0]][t1[1]] = random.randrange(2, 5, 2)
        self.list[t2[0]][t2[1]] = random.randrange(2, 5, 2)
        self.print_board()

    def print_board(self):
        print("""
score:{}
+-----+-----+-----+-----+
|{:^5}+{:^5}+{:^5}+{:^5}+
+-----+-----+-----+-----+
|{:^5}+{:^5}+{:^5}+{:^5}+
+-----+-----+-----+-----+
|{:^5}+{:^5}+{:^5}+{:^5}+
+-----+-----+-----+-----+
|{:^5}+{:^5}+{:^5}+{:^5}+
+-----+-----+-----+-----+
w(up), s(down), a(left), d(right)
q(quit), r(restart)
""".format(self.score, *self.list[0],
           *self.list[1],
           *self.list[2],
           *self.list[3]))

    # 判断输/赢/继续游戏
    def state(self):
        flag = 2
        for x in range(len(self.list)):
            for y in range(len(self.list[x])):
                if self.list[x][y] == 2048:
                    flag = 1  # win
                    break

                if self.list[x][y] == "":
                    self.whiteBoard.append([x, y])
                    flag = 0  # continue

        return flag

    def left(self):
        # 删除空格(2, ,2, )=>(2,2, , )(4, , , )
        # 传入表格每一行 [2," ",2," "]
        for i in range(len(self.list)):
            temp = []
            new_row = []
            # 遍历这行的每个元素,并把非空值传出
            for item in self.list[i]:
                if item:
                    temp.append(item)

            # 得到一个temp[2,2]
            if len(temp) < 1:
                continue

            elif len(temp) < 2:
                new_row.append(temp[0])

            else:
                Flag = True
                for j in range(len(temp)):
                    if Flag:
                        if j + 1 < len(temp) and temp[j] == temp[j + 1]:
                            new_row.append(temp[j] * 2)
                            Flag = False
                        else:
                            new_row.append(temp[j])
                    else:
                        Flag = True
                        # 得到new_row [4]
            y = len(self.list) - (len(new_row))
            # 填补空格
            for x in range(y):
                new_row.append("")
            # 传入表格当前行 [2," ",2," "]=>[4," "," "," "]
            self.list[i] = new_row

    def turn_right(self):
        self.list = [list(x[::-1]) for x in zip(*self.list)]

    def turn_left(self):
        for i in range(3):
            self.turn_right()

            # 随机填补一个随机数

    def add_randNumber(self):
        p = self.whiteBoard.pop(random.randrange(len(self.whiteBoard)))
        # 再随机值
        self.list[p[0]][p[1]] = random.randrange(2, 5, 2)

        self.print_board()

        # 开始游戏

    def start_game(self):

        self.restart()

        # 开始游戏,输入指令
        while True:
            code = input("请输入指令>>>:")
            # 向上?
            if code == "w":
                self.turn_left()
                self.left()
                self.turn_right()

            # 向下?
            elif code == "s":
                self.turn_right()
                self.left()
                self.turn_left()

            # 向左?
            elif code == "a":
                self.left()


            # 向右?
            elif code == "d":
                self.turn_left()
                self.turn_left()
                self.left()
                self.turn_right()
                self.turn_right()


            # 退出
            elif code == "q":
                exit("退出")

            # 重启
            elif code == "r":
                self.restart()

            # 输入有误
            else:
                print("请输入正确的指令！")

            # 判断是否赢了,打印赢了 pass跳出这个游戏状态
            # 判断是否输了,打印输了 pass跳出这个游戏状态

            if self.state() == 1:
                print("You win!")
                break

            if self.state() == 2:
                print("You fail！")
                break

            self.add_randNumber()


if __name__ == "__main__":
    game = Game()
    game.start_game()
