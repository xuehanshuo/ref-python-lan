def sum_numbers(*args):
    ans = 0
    for num in args:
        ans += num

    print(args)
    return ans


result = sum_numbers(1, 2, 3, 4, 5)
print(result)
