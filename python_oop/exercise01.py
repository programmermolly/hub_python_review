# 要求：创建一个类，其中包含若干属性和方法，创建一个对象，调用类中的方法
# 作为面向对象编程的第一份代码，需要写注释。注意，类中要写文档字符串，介绍类的相关信息

def eating(food):
    return '吃%s' % food


class People:
    """
    这个类表示人，内含人的属性和行为
    """

    # 初始化方法
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def sleeping(self, place):
        return '我在%s上睡觉' % place

    def eating(self, food):
        return '吃%s' % food


# 创建对象
people = People('Lily', '女', 23)

# 调用方法
print(people.eating('苹果'))
print(people.sleeping('床'))
