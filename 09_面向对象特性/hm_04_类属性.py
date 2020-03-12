class Tool(object):
    # 相当于静态成员变量
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("Knife")
tool2 = Tool("Gun")
tool3 = Tool("Scope")

print(Tool.count)

# 只会添加 tool3 的实例属性,不会修改类属性
tool3.count = 2
print(Tool.count)
