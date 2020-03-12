# 1.定义元组
info_tuple = ("Jack", 18, 1.75)
print(type(info_tuple))

# 2.访问数据
print(info_tuple[0])

# 3.定义空元组
empty_tuple = ()
print(type(empty_tuple))

# 4.定义单元素元组
single_tuple = (5,)
print(type(single_tuple))

# 5.取索引
print(info_tuple.index(18))

# 6.统计计数
# 单个元素
print(info_tuple.count(17))
# 所有元素
print(len(info_tuple))
