try:
    num = int(input("请输入一个整数: "))

    print(8 / num)

except ZeroDivisionError:
    print("除以了0")

except ValueError:
    print("请输入正确的整数")

    # result 是一个任意标识符,用于接收异常信息
except Exception as result:
    print("%s" % result)

else:
    # 没有异常时候会执行的代码
    pass

finally:
    # 无论何时都会执行的代码
    pass
