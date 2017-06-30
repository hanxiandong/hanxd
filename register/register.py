#coding=utf-8
import base64
from UserDatabase import readUserDatebase,writeUserDatebase
def register(userNameDateBaseList):
    #userNameDateBaseList=readUserDatebase()
    check_use_result=True
    while  check_use_result :
        username=raw_input(u"账号：").strip()

        for  user in userNameDateBaseList:
            if username==user:
                check_use_result=True
                print (u"该用户已经存在请重新输入账号！")
                break
            check_use_result=False
        #账户信息临时缓存列表
        userNameDateBaseList.append(username)

    print(u"新添加的账户：")+userNameDateBaseList[len(userNameDateBaseList)-1]



    check_pwd_result=False
    while not check_pwd_result:
        password=raw_input(u"密码：").strip()
        if len(password)>=6 and len(password)<=8:
            conFirmPassword=raw_input(u"确认密码:").strip()
            if len(conFirmPassword)>=6 and len(conFirmPassword)<=8:
                if password==conFirmPassword:
                    print (u"两次输入的密码一致！")
                    check_pwd_result= True
                else:
                    print(u"两次输入的密码不一致")
                    check_pwd_result= False
            else:
                print (u"请输入6到8位的确认密码！")
                check_pwd_result= False
                continue
        else:
            print (u"请输入6到8位的密码！")
            check_pwd_result= False
            continue
    #base64加密存储
    writeUserDatebase(username,base64.encodestring(password))
    return userNameDateBaseList
#取用户文件中的账号信息

