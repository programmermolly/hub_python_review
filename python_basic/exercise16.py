# 使用while循环改写下列代码（死循环）
# 计算月份
# season = input('请输入季节：')
#
# if season == '春':
#     print('1月、2月、3月')
# if season == '夏':
#     print('4月、5月、6月')
# if season == '秋':
#     print('7月、8月、9月')
# if season == '冬':
#     print('10月、11月、12月')

print('输入q退出！')
while True:
    season = input('请输入季节：')
    if season == '春':
        print('1月、2月、3月')
    if season == '夏':
        print('4月、5月、6月')
    if season == '秋':
        print('7月、8月、9月')
    if season == '冬':
        print('10月、11月、12月')

    if season == 'q':
        break
