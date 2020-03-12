def print_line(char, times):
    """
    打印一条分割线
    :param char: 分割线的字符
    :param times: 分割线字符的个数
    :return: 无
    """
    print(char * times)


def print_lines(char, times, rows):
    i = 0
    while i < rows:
        print_line(char, times)
        i += 1


print_lines("-", 30, 5)
