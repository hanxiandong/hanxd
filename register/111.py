#codingg=utf-8
import time
import datetime
servier_list=['172.21.25.11','172.21.25.12','172.21.30.67','172.21.30.96','172.21.35.18','172.21.35.19']


now_time = datetime.datetime.now()
yes_time = now_time + datetime.timedelta(days=-1)
yes_time_nyr = yes_time.strftime('%Y%m%d')
print yes_time_nyr
log_name="mobile_log/20170629/mobile-apiweb-payment-"+time.strftime("%Y-%m-%d",time.localtime(1))+"-"+servier_list[0]+".log"
with open(log_name,'r') as f:
    tmp=f.readlines()
    #print "----------"+str(tmp.count("card pay error"))
i=0
count=0
for t  in tmp:
    count+=t.count("card pay error")
    if t=="\n":
        print str(i)
    i+=1
print "card pay error:"+str(count)
