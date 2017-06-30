#coding=utf-8
from register import register
from UserDatabase import readUserDatebase
registerState=True
userNameDateBaseList=readUserDatebase()
print(u'开始注册'.center(50,'*'))
while registerState:
    userNameDateBaseList=register(userNameDateBaseList)
    againRegister= raw_input(u"是否还要再次注册(Y/N):").strip()
    if againRegister=="Y" or againRegister=="y":
        pass
    else:
        print(u"注册结束！")
        break