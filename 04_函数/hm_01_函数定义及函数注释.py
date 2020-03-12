# 九九乘法表(2个空行)


def multiple_table():
    """
    九九乘法表
    """
    row = 1
    while row <= 9:

        col = 1
        while col <= row:
            if col != 1:
                print(" ", end="")
            print("%d * %d = %-2d" % (col, row, col * row), end="")
            col += 1

        print("")
        row += 1
