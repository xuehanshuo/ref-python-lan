class Woman:
    def __init__(self, name, age):
        self.name = name
        # 私有属性
        self.__age = age

    # 私有方法
    def __secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))

# 对私有属性只是改了名字,加了 _类名 的前缀
xiaomei = Woman("小美", 18)
print(xiaomei._Woman__age)
xiaomei._Woman__secret()
