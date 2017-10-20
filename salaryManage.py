#!usr/bin/env python
import os
import sys
with open('info.txt','r',encoding='utf-8') as f:
    list=f.read()
list1=list.split('\n')
list2={}
for item in list1:
    item_list=item.split(':')
    list2[item_list[0]]=item_list[-1]
list3=("1、查询员工工资","2、修改员工工资","3、增加新员工","4、退出")
print('功能列表：',list3)
choice=input("请选择功能：")
if choice.isdigit():
    choice=int(choice)
    if choice==1:
        username=input("请输入要查询员工的姓名:")
        if username in list2:
            print(username,'工资：',list2[username])
        else:
            print('查无此人')
    elif choice==2:
        name=input("请输入要修改的员工名字：")
        if name in list2:
            list2[name]=3000
        else:
            print("查无此人")
    elif choice==3:
        name1=input("请输入要增加的员工名字和工资（用冒号分割）:")
        output=open('info.txt','a',encoding='utf-8')
        output.write("\nname1")
        output.close()
    else:
        choice==4
        exit()
else:
    print("请输入数字")








