# 要求：定义父类“动物”，定义其两个子类“狗”和“鸟”
# 借此练习使用issubclass()和isinstance()

class Animal:
    @staticmethod
    def move():
        print('我走了')


class Dog(Animal):
    @staticmethod
    def run():
        print('小狗快跑')


class Bird(Animal):
    @staticmethod
    def fly():
        print('飞高高')


d = Dog()
b = Bird()
d.move()
d.run()
b.move()
b.fly()

# 使用isinstance()
print(isinstance(d, Animal))
print(isinstance(d, Bird))

# 使用issubclass()
print(issubclass(Dog, Animal))
