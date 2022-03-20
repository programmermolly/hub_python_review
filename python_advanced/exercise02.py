# 要求：根据年、月、日，在控制台上显示星期几
# 例如：星期一、星期二、星期三

import time

year = input('年：')
month = input('月：')
day = input('日：')

tuple_time = time.strptime(year + '-' + month + '-' + day, '%Y-%m-%d')
if tuple_time[6] == 0:
    print('星期一')
elif tuple_time[6] == 1:
    print('星期二')
elif tuple_time[6] == 2:
    print('星期三')
elif tuple_time[6] == 3:
    print('星期四')
elif tuple_time[6] == 4:
    print('星期五')
elif tuple_time[6] == 5:
    print('星期六')
elif tuple_time[6] == 6:
    print('星期天')
