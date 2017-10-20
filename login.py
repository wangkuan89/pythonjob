#!usr/bin/env python
import os
import sys

f=open('users.txt','r',encoding='utf-8')            #打开储存用户名的文件
user_s = f.read()                                 #把文件内容读取到user_s里
f.close()                                          #关闭文件
user_list = user_s.split('\n')                     #通过\n 把字符串分割 放入列表user_list里
user_dic={}   #创建一个空字典

#遍历user_list,以字典的形式存入字典 user_dic
for item in user_list:
    item_list = item.split(':')
    user_dic[item_list[0]] = item_list[-1]

#输入名字
username = input("username:")
f1=open('usererror.txt','r',encoding='utf-8')
user_lock=f1.read()
f1.close()
count = 0
if username in user_s:
    if username in user_lock:
        print("帐号已被锁定")
        sys.exit()
    else:
        while count<3:
            password = input("password:")
            if password == user_dic[username]:
                print("登录成功 欢迎%s" % username)
                sys.exit()
            else:
                count+=1
                if count==3:
                    print("您的帐号已被锁定")
                else:
                    print("密码错误，请重新输入")
else:
    print("帐号不存在")




