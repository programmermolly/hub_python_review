# 要求：体会面向对象编程的三大特征：封装、继承、多态
# 1.定义员工管理器，管理员工工资
# 2.定义计算面积的方法
# 计算岗位总工资
# 岗位包括：程序员：底薪+分红
#         销售：底薪+提成
# 注意：添加岗位不能修改员工管理器的代码

class StaffManager:
    def __init__(self):
        self.__staff_salary = []

    def add_staff(self, staff):
        if isinstance(staff, Staff):
            self.__staff_salary.append(staff)

    def get_total_salary(self):
        total_salary = 0
        for item in self.__staff_salary:
            total_salary += item.calculate_salary()
        return total_salary


class Staff:
    def calculate_salary(self):
        pass


class Programmer(Staff):
    def __init__(self, basic_salary, bonus):
        self.b_s = basic_salary
        self.bo = bonus

    def calculate_salary(self):
        return self.bo + self.b_s


class SalesPerson(Staff):
    def __init__(self, basic_salary, income):
        self.b_s = basic_salary
        self.income = income

    def calculate_salary(self):
        return self.income * 0.05 + self.b_s

# 测试
s=SalesPerson(3000,2500)
p=Programmer(15000,2000)
sm=StaffManager()
sm.add_staff(s)
sm.add_staff(p)
print(sm.get_total_salary())



