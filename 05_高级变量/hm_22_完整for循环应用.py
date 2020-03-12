wanted_name = "Jack"
info_list = [{"name": "Tom"},
             {"name": "David"}]

for info in info_list:
    if info["name"] == wanted_name:
        print("We found him, go go go!")
        break;
else:
    print("Nada, we didn't find %s" % wanted_name)
