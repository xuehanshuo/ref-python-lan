"""
str.partition(str1)     把字符串str分成一个3元素的元组(str1前面,str1,str1后面)
str.rpartition(str1)    从右边开始查找
str.split(str1="",num)  以str1为分隔符拆分str为一个列表,如果num有指定值,则仅分隔num+1个子字符串,
                        str1默认包含'\r','\t','\r\n'和空格
str.splitlines()        按照行('\r','\n','\r\n')分隔,返回一个包含各行作为元素的列表
str.join(seq)           以str作为分隔符,将seq中所有的元素(的字符串表示)合并为一个新的字符串
"""
# 1.拆分字符串
poem_str = "\t\n  登鹳雀楼\n王之涣\n\t白日依山尽\t"
poem_list = poem_str.split()
print(poem_list)

# 2.合并字符串
result = " ".join(poem_list)
print(result)
