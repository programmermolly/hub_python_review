# 列表排序
# 要求：把列表[3,80,45,5,7,1]中的元素从小到大排列
# 分析：我们需要将元素两两比较，如果前面的元素大于后面的元素，就将两个元素交换位置
# 取出第一个元素，与后面的元素比较，如果其大于后面的某一元素，则交换二者位置，依次类推，直到满足题目要求

list_numbers = [3, 80, 45, 5, 7, 1]
for i in range(5):
    for n in range(i + 1, 6):

        if list_numbers[i] > list_numbers[n]:
            list_numbers[i], list_numbers[n] = list_numbers[n], list_numbers[i]

        else:
            pass
print(list_numbers)
