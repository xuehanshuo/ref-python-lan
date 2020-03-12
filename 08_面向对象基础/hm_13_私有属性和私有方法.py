class Woman:
    def __init__(self, name, age):
        self.name = name
        # 私有属性
        self.__age = age

    # 私有方法
    def __secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))

# xiaomei = Woman("小美", 18)
