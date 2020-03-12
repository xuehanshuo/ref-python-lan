class Cat:

    def __init__(self, name):
        # 如同构造函数
        print("好可爱的小猫咪!")
        # 定义属性
        self.name = name
        print("%s 闪耀登场" % self.name)

    def __del__(self):
        print("%s 华丽退场" % self.name)


# 此时的Tom对象是全局变量,会在程序进行最后析构
tom = Cat("Tom")
print(tom.name)

# del 关键词删除一个对象,相当于提前调用析构函数
del tom

print("-" * 50)
