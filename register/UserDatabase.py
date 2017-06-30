#coding=utf-8
def readUserDatebase():
    userDataBase = u'register.txt' #用于存放用户信息
    userName_passwordList=[]
    with open(userDataBase, 'r') as userData:
        for  user in userData:
            if  user:
                user=user.split("<<<")[0]
                userName_passwordList.append(user)
            else:
                break
        #原来代码
        #while True:
            #user = userData.readline() # 整行读取用户数据
            #if  user:
                #user=user.split("<<<")[0]
                #userName_passwordList.append(user)
            #else:
                #break
                #print "user="+user
    return    userName_passwordList
def writeUserDatebase(username,password):
    userDataBase = u'register.txt' #用于存放用户信息
    userName_passwordList=[]
    with open(userDataBase, 'a') as userData:
        userData.write("\n"+username+"<<<"+password)
                #print "user="+user


            #p_tmp, E_tmp = [float(i) for i in lines.split()] # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
            #pos.append(p_tmp)  # 添加新读取的数据
            #Efield.append(E_tmp)
        #pass
    #pos = np.array(pos) # 将数据从list类型转换为array类型。
    #Efield = np.array(Efield)
    #pass
#readUserDatebase()