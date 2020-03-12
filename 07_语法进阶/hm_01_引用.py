def test(num):
    print("%d 变量保存的地址是 %d" % (num, id(num)))
    result = "blabla"
    print("%s 的内存地址是 %s" % (result, id(result)))
    return result


# 定义一个数字的变量,数据和变量分开储存,变量储存数据的地址,变量是数据的引用
a = 10

# 地址本质是数字
print("a 变量保存的地址是 %d" % id(a))

# 参数传递的是实参保存的数据的地址,而不是保存的数据本身
ans = test(a)

print("返回值 %s 的地址是 %s" % (ans, id(ans)))

