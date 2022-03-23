# 要求：定义函数，在控制台中获取成绩
# 如果输入有误，则继续获取，直到获取到正确的成绩为止（成绩在0-100之间）

def get_score():
    while True:
        str_score = input('请输入成绩：')
        try:

            score = int(str_score)
        except:
            print('成绩错误!')
            continue

        if 0 <= score <= 100:
            return score




print(get_score())
