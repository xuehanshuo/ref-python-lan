"""
str.isspace()   只包含空格
str.isalnum()   至少有一个字符，且所有字符都是数字或者字母
str.isalpha()   至少有一个字符，且所有字符都是字母
str.isdecimal() 只包含数字，全角数字
str.isdigit()   只包含数字，全角数字，⑴，\u00b2
str.isnumeric() 只包含数字，全角数字，⑴，\u00b2，汉字数字
str.istitle()   标题化的（每个单词首字母大写）
str.islower()   包含至少一个区分大小写的字符，且这些区分大小写的字符都是小写
str.isupper()   包含至少一个区分大小写的字符，且这些区分大小写的字符都是大写
"""
# 1.判断空白字符
space_str = "   \n"
print(space_str.isspace())

# 2.判断字符串中是否只含有数字
# 1>都不能判断小数
# num_str = "1.1"
# 2>第一个不能判断unicode字符串
num_str = "\u00b2"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
# 3>最后一个能判断中文数字
num_str2 = "一千零一"
print(num_str2)
print(num_str2.isdecimal())
print(num_str2.isdigit())
print(num_str2.isnumeric())
