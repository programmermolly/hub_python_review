# 要求：构建函数my_enumerate实现enumerate()的功能
def my_enumerate(list_):
    count = 0
    for item in list_:
        yield(count,item)
        count+=1




if __name__=='__main__':
    list_given=[1,2,4,7,9]
    for index,item in my_enumerate(list_given):
        print(index,item)