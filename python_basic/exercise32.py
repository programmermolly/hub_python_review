# 录入所有学生成绩，输入空字符串表示结束
# 打印所有成绩
# 计算最高分、最低分、平均分

scores=[]
while True:
    score = input('请输入学生成绩，按enter键结束（每次只能输入一个成绩）：')
    if score=='':
        break
    scores.append(int(score))

for item in scores:
    print(item)

print('最高分为：'+str(max(scores)))
print('最低分为：'+str(min(scores)))
print('平均分为：'+str(sum(scores)/len(scores)))

    

