# 1.格式化字符串就是由字符串和元组拼接的字符串
info_tuple = ("Jack", 18, 1.85)
print("%s 的年龄是 %d ,身高是 %.2f" % info_tuple)

info_str = "%s 的年龄是 %d ,身高是 %.2f" % info_tuple
print(info_str)

# 2.list和tuple进行相互转化
info_list = list(info_tuple)
info2_tuple = tuple(info_list)
