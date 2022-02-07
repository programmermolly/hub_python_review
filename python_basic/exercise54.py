# 集合的运算
# 要求：一家公司的人员如下所示：
# 经理：曹操、刘备、孙权
# 技术人员：曹操、刘备、张飞、关羽

# 请回答：
# 谁既是经理又是技术人员？
# 谁是经理但不是技术人员？
# 谁是技术人员但不是经理？
# 张飞是经理吗？
# 找出所有只有一个岗位的人员
# 经理和技术人员总共有多少人？

managers = {'曹操', '刘备', '孙权'}
engineers = {'曹操', '刘备', '张飞', '关羽'}
# 1.
print('第一题：' + str(managers & engineers))
# 2.
print('第二题：' + str(managers - engineers))
# 3.
print('第三题：' + str(engineers - managers))
# 4.
print('第四题：' + str('张飞' in managers))
# 5.
print('第五题：' + str((engineers | managers) - (engineers & managers)))
# 6.
print('第六题：' + str(len(engineers | managers)))
