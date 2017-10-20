#!usr/bin/env python


menu = {"北京":{"朝阳":{"国贸":{},"望京":{},"亚运村":{}},
                "海淀":{"中关村":{},"上地":{},"五棵松":{}},
                 "东城区":{"东直门":{},"王府井":{},"前门":{}}},
        "上海":{"黄浦区":{"新天地":{},"外滩":{}},
                "徐汇区":{"徐家汇":{},"龙华":{}},
                "宝山区":{"大场":{},"七宝":{}}},
        "天津":{"南开区":{"黄河道":{},"鼓楼":{}},
                "滨海新区":{"解放路":{},"新港":{}},
                "虹桥区":{"芥园道":{},"五大道":{}}}
        }
while True:
    for key in menu:
        print(key)
    choice = input(">>:").strip()
    if len(choice) == 0:continue
    if choice == "b":break
    if choice not in menu:continue

    while True:
        for key2 in menu[choice]:
            print(key2)
        choice2 = input(">>:").strip()
        if len(choice2) == 0: continue
        if choice2 == "b": break
        if choice2 not in menu[choice]: continue

        while True:
            for key3 in menu[choice][choice2]:
                print(key3)
            choice3 = input(">>:").strip()
            if len(choice3) == 0:continue
            if choice3 == "b":
                break
            if choice3 == "q":
                exit()
            if choice3 not in menu[choice][choice2]: continue

            while True:
                for key4 in menu[choice][choice2][choice3]:
                    print(key4)
                choice4 = input(">>:").strip()
                if len(choice4) == 0: continue
                if choice4 == "b": break
                if choice4 not in menu[choice][choice2][choice3]: continue
