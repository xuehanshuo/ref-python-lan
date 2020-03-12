xiaoming = {"name": "小明"}

# 1.访问
print(xiaoming["name"])

# 2.增加/修改
# 不存在，新增键值对
xiaoming["height"] = 1.85
# 存在，修改value的内容
xiaoming["name"] = "大明"

# 3.删除
# 无默认参数，必须指定一个存在的key值
xiaoming.pop("name")

print(xiaoming)
