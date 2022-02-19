# 要求：编写一个可以计算斤和两的函数
# # 计算斤两
# liang_user=int(input('请输入两数：'))
# jin=liang_user//16
# liang=liang_user%16
# print('这是'+str(jin)+'斤'+str(liang)+'两')

def calculate_jin_liang(liang_user):
    """
    计算斤两的函数
    """
    jin = liang_user // 16
    liang = liang_user % 16
    return jin, liang


# 测试函数
liang_user = int(input('请输入两数：'))
print('这是%d斤%d两' % calculate_jin_liang(liang_user))
