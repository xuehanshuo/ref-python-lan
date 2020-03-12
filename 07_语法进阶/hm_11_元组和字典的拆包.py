def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_nums = (1, 2, 3)
gl_dict = {"name": "小明",
           "age": 18}

# 拆包语法,简化参数传递的过程
# 元组前一个 * ,字典前两个 *
demo(1, 2, 3, name="小明", age=18)
demo(*gl_nums, **gl_dict)
