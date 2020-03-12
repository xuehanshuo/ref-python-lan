# i = 0
# c = 9
#
# while i < 5:
#     print("Hello!")
#     c **= i
#     # c //= i
#     # i = i + 1
#     i += 1
#
# print(c)

result = 0

i = 0
while i <= 100:
    if i == 1:
        i += 1
        continue

    if i == 5:
        break

    if (i % 2 == 0) is False:
        print(i)
        result += i

    i += 1

print("The answer should be: %d" % result)
