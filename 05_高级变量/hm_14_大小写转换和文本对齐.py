"""
str.capitalize()    把第一个字符大写
str.title() 把字符串每个单词首字母大写
str.lower() 大写变小写
str.upper() 小写变大写
str.swapcase()  大小写翻转

str.ljust(width)    返回一个原字符串左对齐，使用空格填充至长度width的新字符串
str.rjust(width)    返回一个原字符串右对齐，使用空格填充至长度width的新字符串
str.center(width)   返回一个原字符串居中，使用空格填充至长度width的新字符串
"""
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽"]
for sent in poem:
    print("|%s|" % sent.center(10, " "))

