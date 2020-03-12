class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 判断是否有子弹
        if self.bullet_count == 0:
            print("%s 已经没有子弹了" % self.model)
            return

        # 发射子弹
        self.bullet_count -= 1

        # 提示成功,显示剩余子弹
        print("%s 突突突... 还剩 [%d] 发子弹" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        # 1.姓名
        self.name = name

        # 2.新兵没有枪,使用关键字 None
        self.gun = None

    def fire(self):
        # 1.判断有没有枪
        # 身份运算符 is 和 is not 用来判断两个标识符是否引用同一个对象
        # == 用于判断引用变量的值是否相等
        if self.gun is None:
            print("[%s] 还没有枪..." % self.name)

        # 2.高喊口号
        print("冲鸭!...%s" % self.name)

        # 3.装填子弹
        self.gun.add_bullet(100)

        # 4.开火
        self.gun.shoot()


# 1.创建枪对象
ak47 = Gun("AK47")

# 2.创建士兵
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
print(xusanduo.gun)

# 3.士兵开枪
xusanduo.fire()
