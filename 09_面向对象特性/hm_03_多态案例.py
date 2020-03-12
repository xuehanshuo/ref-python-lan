class GodA(object):
    def fire(self):
        print("cast a GodA fire...")


class GodB(object):
    def fire(self):
        print("cast a GodB fire...")


class Person(GodA, GodB):

    def fire(self):
        print("cast a Human fire...")


# 因为不用声明类型,所以不明显
# 理解为鸭子模型
def cast_fire(obj):
    obj.fire()


cast_fire(GodB())
cast_fire(GodA())
cast_fire(Person())
