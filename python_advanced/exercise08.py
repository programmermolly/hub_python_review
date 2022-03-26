# 要求：创建员工管理器，将其变为可迭代对象，并迭代

class Employee:
    pass


class EmployeeManager:
    def __init__(self):
        self.__employees = []

    def add_employee(self, emp):
        self.__employees.append(emp)

    def __iter__(self):
        return EmployeeIterator(self.__employees)


class EmployeeIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


if __name__ == '__main__':
    em = EmployeeManager()
    em.add_employee(Employee())
    em.add_employee(Employee())
    em.add_employee(Employee())

    iterator = em.__iter__()
    while True:
        try:
            item = iterator.__next__()
        except StopIteration:
            break
        print(item)
