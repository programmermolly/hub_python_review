from linklist import *
from time import time

list_test = list(range(999999))
for item in list_test:
    print(item)
link_list = LinkList()
link_list.init_list(list_test)
tm = time()
link_list.traversing_list()
link_list.head_insert(8866)
link_list.insert(100,999)

print('time:', time() - tm)
