class Game(object):
    __top_score = 0

    @classmethod
    def show_top_score(cls):
        print(cls.__top_score)

    @staticmethod
    def show_help():
        print("Just follow your heart!")

    def __init__(self, name):
        self.name = name

    def start_game(self):
        print("%s is gaming now..." % self.name)


# 静态方法
Game.show_help()

# 类方法
Game.show_top_score()

# 实例方法
game = Game("小明")
game.start_game()
