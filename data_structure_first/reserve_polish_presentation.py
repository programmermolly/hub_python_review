# 要求：编写程序，计算逆波兰表达式的值

from sstack import *

st=SStack()
usr_input=input()
tmp=usr_input.split(' ') # 结果为列表
for item in tmp:
    if item not in ['+','-','*','/','p']:
        st.push(int(item))
    elif item=='+':
        y=st.pop()
        x=st.pop()
        st.push(x+y)
    elif item=='-':
        y = st.pop()
        x = st.pop()
        st.push(x - y)
    elif item=='*':
        y = st.pop()
        x = st.pop()
        st.push(x * y)
    elif item=='/':
        y = st.pop()
        x = st.pop()
        st.push(x / y)
    elif item=='p':
        print(st.top())


