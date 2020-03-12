def print_info(name, title="", gender=True):
    """

    :param title:职位
    :param name: 同学姓名
    :param gender: True 男生, False 女生
    :return:
    """
    gender_test = "男生"
    if not gender:
        gender_test = "女生"

    print("[%s]%s 是 %s" % (title, name, gender_test))


# 指定对哪个有默认参数的形参赋值
print_info("小美", gender=False)
