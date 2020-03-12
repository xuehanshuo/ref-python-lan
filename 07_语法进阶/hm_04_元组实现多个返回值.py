def measure():
    print("开始测试")
    temp = 89
    wetness = 100
    print("测试结束")

    # 返回类型是元组,小括号可以省略
    return temp, wetness


result = measure()
print(result)

# 单独处理温度湿度
# 如果函数返回的类型是元组,同时希望单独处理元组中的元素
# 可以使用多个变量,一次性接收函数的返回结果,个数必须保持一致
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)
