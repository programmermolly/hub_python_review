# 要求： 将python_oop/exercise09.py导入此模块，并完成当时的练习题

import exercise01_relevant_module

list_given = [
    ['00', '01', '02', '03'],
    ['10', '11', '12', '13'],
    ['20', '21', '22', '23'],
]
# 1.
pos01 = exercise01_relevant_module.Vector2(1, 3)
dir01 = pos01.left()
res_receive01 = exercise01_relevant_module.get_elements(list_given, pos01, dir01, 3)
print('res_receive01=' + str(res_receive01))

# 2.
pos02 = exercise01_relevant_module.Vector2(2, 2)
dir02 = pos02.up()
res_receive02 = exercise01_relevant_module.get_elements(list_given, pos02, dir02, 2)
print('res_receive02=' + str(res_receive02))

# 3.
pos03 = exercise01_relevant_module.Vector2(0, 3)
dir03 = pos03.down()
res_receive03 = exercise01_relevant_module.get_elements(list_given, pos03, dir03, 2)
print('res_receive03=' + str(res_receive03))


