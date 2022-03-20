# 根据你的生日，计算你活了多少天
# 2000.6.12

import time

tuple_time_birth = time.strptime('2000-6-12', '%Y-%m-%d')
unix_stamp_now = time.time()
tuple_time_now = time.localtime(unix_stamp_now)
age = (tuple_time_now[0] - tuple_time_birth[0]) * 365
print(age)
