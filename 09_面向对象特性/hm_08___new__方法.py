class MusicPLayer(object):

    def __new__(cls, *args, **kwargs):
        # 1.创建对象时,new房子自动被调用
        print("__new__ is called")

        # 2.为对象分配空间,静态方法需要传入参数
        instance = super().__new__(cls)

        # 3.返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")


player = MusicPLayer()
print(player)
