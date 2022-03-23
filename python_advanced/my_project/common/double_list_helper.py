class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def test1(self):
        return self.x + self.y

    @staticmethod
    def test2():
        print('算出来了吗？')
