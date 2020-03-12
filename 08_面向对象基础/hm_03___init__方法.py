class Cat:

    def __init__(self, name):
        # 如同构造函数
        print("好可爱的小猫咪!")
        # 定义属性
        self.name = name


tom = Cat("Tom")
print(tom.name)
