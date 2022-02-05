# 将1970年到2050中的闰年存入列表（使用列表推导式）
# 闰年 leap year
leap_year = [year for year in range(1970, 2051) if year % 4 == 0 or year % 100 != 0 and year % 400 == 0]
print(leap_year)
