num_list = [3, 2, 1]
name_list = ["one", "two", "four"]

# 1.统计
# len 统计元素的总数
print(len(num_list))
# count 统计某一个数据出现的次数
print(num_list.count(-100))

# 2.排序
# 升序
num_list.sort()
name_list.sort()
# 降序
num_list.sort(reverse=True)
name_list.sort(reverse=True)
# 反转，逆序
num_list.reverse()
name_list.reverse()

print(num_list)
print(name_list)
