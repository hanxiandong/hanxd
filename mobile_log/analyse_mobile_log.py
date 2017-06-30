#coding=utf-8
import time
import datetime

def analyse_mobile_log(log_name,keyWord):

    #log_name="mobile_log/20170629/mobile-apiweb-payment-"+str(yes_time_nyr)+"-"+servier_list[0]+".log"
    with open(log_name,'r') as f:
        tmp=f.readlines()
        #print "----------"+str(tmp.count("card pay error"))
    i=0
    count=0
    for t  in tmp:
        count+=t.count(keyWord)
        if t=="\n":
            #print str(i)
         pass
        i+=1
    #print "card pay error:"+str(count)
    return count
