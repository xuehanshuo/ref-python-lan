class Tool(object):
    __count = 0

    # 装饰器
    @classmethod
    def show_tool_count(cls):
        print("一共有 %d 个工具" % cls.__count)

    def __init__(self, name):
        self.name = name
        Tool.__count += 1


tool1 = Tool("Knife")
tool2 = Tool("Gun")
tool3 = Tool("Scope")

Tool.show_tool_count()
