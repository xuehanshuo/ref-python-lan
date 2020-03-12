class GodA:
    def fire(self):
        print("cast a GodA fire...")


class GodB:
    def fire(self):
        print("cast a GodB fire...")


class Person(GodA, GodB):

    def fire(self):
        super().fire()
        print("cast a Human fire...")


xiaoming = Person()
xiaoming.fire()

# 但这种重名的情况应该避免使用多继承
print(Person.__mro__)
