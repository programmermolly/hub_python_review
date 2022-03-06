"""
项目：1.完成数据模型类
     2.完成逻辑控制类
     3.完成数据__student_list
     4.获取列表方法stu_list
     5.添加学生方法add_student
     6.根据编号删除学生remove_student
     7.修改学生信息update_student
     8.在试图类中根据编号删除学生




"""


class StudentModel:
    """
    数据
    """

    def __init__(self, name, age=0, score=0, id=0):
        self.name = name
        self.stu_id = id
        self.age = age
        self.score = score


class StudentManagementController:
    __init_id = 1  # 初始id

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, student_info):
        """
        添加学生
        :param student_info: 学生信息

        """
        student_info.stu_id = self.__generate_id()
        self.__stu_list.append(student_info)

    def __generate_id(self):
        StudentManagementController.__init_id += 1
        return StudentManagementController.__init_id

    def remove_student(self, id):
        for item in self.__stu_list:
            if item.stu_id == id:
                self.__stu_list.remove(item)
                return True  # 移除成功
        return False  # 移除失败

    def update_student(self, stu_info):
        for item in self.__stu_list:
            if stu_info.stu_id == item.stu_id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True  # 修改成功
        return False  # 修改失败


class StudentManagementView:
    def __init__(self):
        self.__management = StudentManagementController()

    def __display_menu(self):
        print('1)添加学生')
        print('2)显示学生')
        print('3)删除学生')
        print('4)修改学生')
        print('5)按照成绩升序显示学生')

    def __select_menu(self):
        item = input('请输入：')
        if item == '1':
            self.__input_student()
        elif item == '2':
            self.__output_student(self.__management.stu_list)
        elif item == '3':
            self.__delete_student()
        elif item == '4':
            self.__modify_student()
        elif item == '5':
            pass

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        name = input('请输入姓名：')
        age = int(input('请输入年龄：'))
        score = int(input('请输入成绩：'))
        stu = StudentModel(name, age, score)
        self.__management.add_student(stu)

    def __output_student(self, output_list):
        for item in output_list:
            print(item.stu_id, item.name, item.age, item.score)
    def __delete_student(self):
        stu_id=int(input('请输入学生编号：'))
        if self.__management.remove_student(stu_id):
            print('删除成功！')
        else:
            print('删除失败！')
    def __modify_student(self):
        stu_id=int(input('请输入编号：'))
        new_name=input('请输入新的姓名：')
        new_age=int(input('请输入新的年龄：'))
        new_score=int(input('请输入新的成绩：'))
        new_stu=StudentModel(new_name,new_age,new_score)
        if self.__management.update_student(new_stu):
            print('修改成功！')
        else:
            print('修改失败！')




view=StudentManagementView()
view.main()