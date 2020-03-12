class God:
    def fire(self):
        print("cast a God fire...")


# 1.发生了继承
class Person(God):

    # 2.进行了复写
    def fire(self):
        # 3.使用super()类,保留父类方法作为子类方法的一部分
        # 父类名.方法(self) 在Python 2.x中使用,不推荐
        # God.fire(self)
        super().fire()
        print("cast a Human fire...")


xiaoming = Person()
xiaoming.fire()
