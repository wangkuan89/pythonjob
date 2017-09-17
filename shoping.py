#!usr/bin/env python
products = [
          ["iphone",5000],
          ["MAC",10000],
          ["Book",300],
          ["water",200],
          ["clothes",500],
]
shoping_list = []          #商品列表

#把输入的字符串转换为数字
while True:
    salary=input("请输入你的工资：")
    if salary.isdigit():
        salary=int(salary)
        break
    else:
        continue

while True:
    print("商品列表".center(30, "-"))
    for index,i in enumerate(products):
        print(index,'.',i[0],i[1])  #用enumerate函数可以把列表遍历为带索引的商品列表
    choice = input("请输入商品编号>>:")
    if choice.isdigit():
        choice= int(choice)
        if choice>=0 and choice< len(products):
            m = products[choice]
            if salary>=m[1]:
                salary-=m[1]
                shoping_list.append(m)
                print("商品已加入你的购物车，你的当前余额:{}" .format(salary))
            else:
                print("钱不够，你只有{}" .format(salary))
        else:
            print("商品不存在")
    elif choice=="q":
        print("已购买商品".center(30,"-"))
        for i in shoping_list:
            print(i)
        print("你的余额为:{}".format(salary))
        exit()
    else:
        print("商品编号应为数字")