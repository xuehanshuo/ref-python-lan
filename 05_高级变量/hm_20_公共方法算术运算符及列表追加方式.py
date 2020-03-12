"""
+               合并,不支持字典
*               重复,不支持字典
in              元素是否存在,支持字典     3 in (1,2,3)
not in          元素是否不存在,支持字典   4 not in (1,2,3)
> >= == <= <    元素比较,不支持字典      (1,2,3) < (2,2,3)

in 和 not in 为成员运算符,判断字典时针对的是 key
"""
# 不会修改原来的list,生成新的
list_temp = ([1, 2] + [3, 4]) * 2
print(list_temp)

# 正常分解元素插入,修改原来的list
list_temp.extend([5, 6])
print(list_temp)

# [7,8]将被认为是一个新类型,作为一个新元素追加到list中
list_temp.append([7, 8])
print(list_temp)
