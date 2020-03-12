"""
else中的语句只有在完全遍历整个循环后才会执行,使用break中途退出则不会执行
"""
for num in (1, 2, 3):
    print(num)
    # if num == 2:
    # break
else:
    print("Try it!")

print("The End")
