"""
用于:函数参数的 个数 不确定
用法:参数名前加一个 * ,可以接收元组
    参数名前加两个 * ,可以接收字典
惯用法:元组参数 *args , 字典参数 **kwargs
"""


def demo(num, *args, **kwargs):
    print(num, args, kwargs)


demo(1, 2, 3, 4, 5)
# 向字典传参数与多个缺省参数的格式一样
demo(1, 2, 3, name="123", age=18)
