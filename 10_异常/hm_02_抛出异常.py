def input_password():
    pwd = input("请输入密码: ")

    if len(pwd) >= 8:
        return pwd

    print("主动抛出异常")
    # 创建异常变量 - 使用错误信息字符串作为参数
    ex = Exception("密码长度不够")
    # 抛出异常
    raise ex


try:
    print(input_password())
except Exception as result:
    print(result)
