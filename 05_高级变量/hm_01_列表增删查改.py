name_list = ["one", "two", "three"]
"""
name_list.
      name_list.append  name_list.count   name_list.insert  name_list.reverse 
      name_list.clear   name_list.extend  name_list.pop     name_list.sort    
      name_list.copy    name_list.index   name_list.remove 
"""
# 1.取值和取索引
# 取值
print(name_list[0])
# 取索引
print(name_list.index("one"))

# 2.修改数据
name_list[0] = "ones"

# 3.增加
# append 向列表末尾追加数据
name_list.append("one")
# insert
name_list.insert(1, "zero")
# extend 把其他列表追加到末尾
name_list_temp = ["uno", "dos"]
name_list.extend(name_list_temp)

# 4.删除
# remove 删除第一个指定的数据
name_list.remove("ones")
# pop 默认弹出并返回最后一个变量，否则删除对应索引值
name_list.pop()
name_list.pop(4)
# clear 清空列表
name_list.clear()
# del 用于从内存中删除某个变量，后续代码不可再使用这个变量
"""
del name_list[0]

name = "one"
del name
print(name)  # 不可用
"""

print(name_list)
