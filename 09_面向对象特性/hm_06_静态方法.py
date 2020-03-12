# 不需访问实例属性,实例方法
# 不需访问类属性,类方法


class Dog(object):
    @staticmethod
    def run():
        print("来了来了!")


Dog.run()
