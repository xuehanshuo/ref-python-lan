"""
shebang
import模块
全局变量
函数定义
执行代码

gl_前缀
g_前缀
"""
g_num = 10


def demo01():
    print(g_num)
    print(gl_title)
    # print(name)


# title可以被识别,因为在调用前定义了,程序找到了它的定义
gl_title = "123"

demo01()

# name不可以
# name = "123456"
