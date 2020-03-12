has_ticket = True
knife_length = 30

if has_ticket:
    print("Please hand over your knife and let us check it")
    if knife_length > 20:
        print("You are a killer? You have a %d cm knife!" % knife_length)
        print("I am sorry to inform you that you can't enter")
    else:
        print("You are free to pass, have a nice day!")
else:
    print("Please buy one ticket first!")
