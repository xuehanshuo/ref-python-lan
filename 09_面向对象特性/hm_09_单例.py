class MusicPLayer(object):
    # 记录第一次创建的实例对象地址
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 没有对象则分配空间
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        if not self.init_flag:
            self.init_flag = True
            print("播放器初始化")


player1 = MusicPLayer()
print(player1)
player2 = MusicPLayer()
print(player2)
