xiaoming = {"name": "小明",
            "age": 18}

# 1.统计键值对数量
print(len(xiaoming))

# 2.合并字典
# 如果被合并的字典中出现已经存在的键值对，更新该键值对
temp_dic = {"height": 1.85,
            "age": 20}
xiaoming.update(temp_dic)

# 3.清空字典
xiaoming.clear()

print(xiaoming)
