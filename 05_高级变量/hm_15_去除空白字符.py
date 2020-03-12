"""
str.lstrip()    截掉str左边开始的空白字符
str.rstrip()    截掉str右边末尾的空白字符
str.strip()     截掉str左右两边的空白字符
"""
poem = ["\t\n登鹳雀楼",
        "王之涣\n",
        "白日依山尽\t"]
for sent in poem:
    print("|%s|" % sent.strip().center(10, " "))
