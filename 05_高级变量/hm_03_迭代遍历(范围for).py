# 1.list字典
name_list = ["one", "two", "four"]
for name in name_list:
    print("The name is : %s" % name)
print("---------------------")

# 2.tuple元组
info_tuple = ("Jack", 18, 1.75)
for info in info_tuple:
    print(info)
print("---------------------")

# 3.dictionary字典
xiaoming_dic = {"name": "小明",
                "qq": "123456",
                "phone": "123456789"}
for k in xiaoming_dic:
    print("%s - %s" % (k, xiaoming_dic[k]))
print("---------------------")