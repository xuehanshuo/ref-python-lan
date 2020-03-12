def say_hello():
    print("la la la")


# 直接执行永远都是__main__
# 被导入之后变成 模块名
if __name__ == "__main__":
    print(__name__)

    say_hello()
