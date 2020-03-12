def demo(num, num_list):
    # num = num + num
    num += num

    # 列表变量
    # 本质是是调用了列表的 extend 方法
    num_list += num_list

    print(num)
    print(num_list)


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
