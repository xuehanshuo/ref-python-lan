"""
这是无奈之举
python不要求提供类型名,所以在函数内部的修改操作优先被看做是重新定义一个同名变量
导致了所谓的"不能直接修改"
"""
num = 10


def demo01():
    global num
    num = 99
    print(num)


demo01()
print(num)
