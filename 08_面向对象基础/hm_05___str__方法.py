class Cat:

    def __init__(self, name):
        # 如同构造函数
        print("好可爱的小猫咪!")
        # 定义属性
        self.name = name
        print("%s 闪耀登场" % self.name)

    def __del__(self):
        print("%s 华丽退场" % self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "我是小猫[%s]!" % self.name


tom = Cat("Tom")
print(tom)
