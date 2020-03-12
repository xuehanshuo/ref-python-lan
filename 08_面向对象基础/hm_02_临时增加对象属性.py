class Cat:
    # self是调用对象的引用
    def eat(self):
        print("%s 要吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


tom = Cat()

# 添加 name 属性
tom.name = "Tom"

tom.eat()
tom.drink()
