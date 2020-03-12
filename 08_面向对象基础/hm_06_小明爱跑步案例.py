class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print(self.__str__())

    def __str__(self):
        return "我就是 %s , 我的体重是 %.2f" % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5
        print("我爱跑步!")

    def eat(self):
        self.weight += 1
        print("我爱吃东西!")


xiaoming = Person("小明", 75)

xiaoming.eat()
xiaoming.run()

print(xiaoming)
