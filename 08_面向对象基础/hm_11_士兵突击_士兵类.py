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


# 1.创建枪对象
ak47 = Gun("AK47")
ak47.add_bullet(100)
ak47.shoot()

# 2.创建士兵
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
print(xusanduo.gun)
