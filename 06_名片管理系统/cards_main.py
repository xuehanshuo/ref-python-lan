#! /usr/bin/python3
"""
0.每一步操作的上方添加注释,将任务细分,函数需要添加函数注释
1.框架搭建,使用无限循环,pass,TODO等辅助,保证程序可以正常运行(用户输入任何信息都可以有对应)
2.框架函数搭建,用框架函数替换pass的内容

3.确定数据结构,初始化数据结构
4.针对用户的每个操作,都需要有回应,成功或者失败或者结果
5.高内聚,低耦合,易维护
"""
import cards_tools

while True:
    # 显示欢迎界面
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作: ")
    print("您选择的操作是:[%s]" % action_str)

    # pass 表示一个占位符,表示程序代码结构正确,相当于空大括号
    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards_tools.new_card()
        elif action_str == "2":
            cards_tools.show_all()
        elif action_str == "3":
            cards_tools.search_card()

    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用[名片管理系统]")
        break

    # 其他内容输入错误,提示用户
    else:
        print("您输入的不正确,请重新选择")
