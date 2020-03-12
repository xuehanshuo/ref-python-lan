num_list1 = [1, 2, 3]


def demo01(num_list):
    # 对可变参数的赋值被看做改变了原有数据的引用
    # num_list = [4, 5, 6]
    # print(num_list)
    # print(num_list1)

    # 没有改变引用的意图,只是修改引用中的数据
    num_list.append(4)
    print(num_list)
    print(num_list1)


demo01(num_list1)
