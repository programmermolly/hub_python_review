from python_advanced import exercise08

em_08 = exercise08.EmployeeManager()

em_08.add_employee(exercise08.Employee())
em_08.add_employee(exercise08.Employee())
em_08.add_employee(exercise08.Employee())
em_08.add_employee(exercise08.Employee())
em_08.add_employee(exercise08.Employee())

for item in em_08:
    print(item)
