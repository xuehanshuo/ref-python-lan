num_str = "0123456789"

# 1.截取 2 - 5 位置的字符串
print(num_str[2:6])

# 2.截取 2 - 末尾 的字符串
print(num_str[2:])

# 3.截取 0 - 5 位置的字符串
print(num_str[:5])
print(num_str[0:5])

# 4.截取完整的字符串
print(num_str[:])

# 5.从开始位置,每隔一个字符截取字符串
print(num_str[::2])

# 6.从索引 1 开始,每隔一个取一个
print(num_str[1::2])

# 7.截取从 2 - 末尾-1 的字符串
print(num_str[2:-1])

# 8.截取字符串末尾两个字符
print(num_str[-2:])

# 9.取得逆序字符串
print(num_str[-1::-1])
print(num_str[::-1])
