a = 6
b = 10

# 解法一:三变量法
# t = a
# a = b
# b = t

# 解法二:不使用其他的变量
# a = a + b
# b = a - b
# a = a - b

# 解法三:Python专有,利用元组
# a, b=(b, a) 左边是变量,右边是省略小括号的元组
a, b = b, a

print(a, b)
