"""
str.startswith(str) 是否以str开头
str.endswith(str)   是否以str结束
str.find(str1,start=0,end=len(str))  str1是否包含在该字符串指定区域中，返回开始的索引值或者-1
str.rfind(str1,start=0,end=len(str))    从右边开始查找
str.index(str1,start=0,end=len(str))    str1不在会报错
str.rindex(str1,start=0,end=len(str))   从右边开始查找
str.replace(old_str,new_str,num=str.count(old_str)) 把old_str替换成new_str，num指定则不超过num次替换，
                                                    返回新字符串，不改变旧字符串
"""
hello_str = "Hello World"
# 1.是否以str开头
print(hello_str.startswith("Hel"))
# 2.是否以str结束
print(hello_str.endswith("ld"))
# 3.查找
print(hello_str.find("lo"))
print(hello_str.find("123"))
# 4.替换
print(hello_str.replace("World", "World!"))
print(hello_str)
