# 输入月份，显示天数
# 注：1、3、5、7、8、10、12月有31天
#     2月有28天（不考虑闰年）
#     其余月份有30天

month=input('请输入月份：')
if month=='1'or month=='3'or month=='5'or month=='7'or month=='8'or month=='10'or month=='12':
    print('该月有31天')
if month=='2':
    print('该月有28天')
if month=='4'or month=='6'or month=='9'or month=='11':
    print('该月有30天')
if month>'12':
    print('输入有误！')