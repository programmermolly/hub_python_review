# 使用元组优化下列代码

# month=input('请输入月份：')
# if month=='1'or month=='3'or month=='5'or month=='7'or month=='8'or month=='10'or month=='12':
#     print('该月有31天')
# if month=='2':
#     print('该月有28天')
# if month=='4'or month=='6'or month=='9'or month=='11':
#     print('该月有30天')
# if month>'12':
#     print('输入有误！')

month = input('请输入月份：')
if int(month) in (1, 3, 5, 7, 8, 10, 12):
    print('该月有31天')
if month == '2':
    print('该月有28天')
if int(month) in (4, 6, 9, 11):
    print('该月有30天')
if int(month) > 12:
    print('输入有误！')


