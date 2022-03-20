# 每个类其实都重写了__str__和__repr__方法
# 因此我们才能打印它们的对象
# 例如：打印自定义的列表

class Student:
    def __init__(self, name, age, score, gender):
        self.name = name
        self.age = age
        self.score = score
        self.gender = gender

    def __str__(self):
        return '我叫%s，年龄%s，成绩%s，性别%s' % (self.name, self.age, self.score, self.gender)

    def __repr__(self):
        return 'Student("%s",%s, %s, "%s")' % (self.name, self.age, self.score, self.gender)


s_learner = Student('jx', 21, 100, '男')
print(s_learner)
str_test = str(s_learner)
print(str_test)
repr_test = repr(s_learner)
print(repr_test)

# eval()函数
res = eval('1*2+5')
print(res)

# 克隆对象
s_learner_copy = eval(repr(s_learner))
print(type(s_learner))
print(type(s_learner_copy))
