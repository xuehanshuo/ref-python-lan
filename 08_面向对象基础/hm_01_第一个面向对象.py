class Cat:
    def eat(self):
        print("小猫要吃鱼")

    def drink(self):
        print("小猫要喝水")


tom = Cat()
tom.eat()
tom.drink()

print(tom, "\n", id(tom))
