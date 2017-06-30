#coding=utf-8
import os
import time
import datetime
from  analyse_mobile_log  import analyse_mobile_log
servier_list=['172.21.25.11','172.21.25.12','172.21.30.67','172.21.30.96','172.21.35.18','172.21.35.19']
#dfasdfasdfdasf
#统计昨天（yes_time_nyr）
now_time = datetime.datetime.now()
yes_time = now_time + datetime.timedelta(days=-1)
yes_time_nyr = yes_time.strftime('%Y-%m-%d')
#print u"昨天："+yes_time_nyr
#统计今天（now_time）
now_time = datetime.datetime.now()
now_time=now_time.strftime('%Y-%m-%d')
#print u"今天："+now_time
keyWord="card pay error"
total=0
count_list=[]
log_size=0
for ip in servier_list:
    #print ("ip")+ip
    log_name="mobile_log/20170629/mobile-apiweb-payment-"+str(yes_time_nyr)+"-"+ip+".log"
    #print "log_name"+log_name
    log_url="C:\\Users\\hanxiandong\\PycharmProjects\\untitled\\register\\"+log_name
    log_size+=os.path.getsize(log_url)
    #print log_size
    print ip+" "+('%d Bytes'%(os.path.getsize(log_url)))
    #分析日志
    count=analyse_mobile_log(log_name,keyWord)
    total+=count
    count_list.append(ip+"+"+str(count))

print str(yes_time_nyr)+""
print keyWord+":"+str(total)
print keyWord+":"+str(log_size)+"Bytes"
for error_count in count_list:
    ip=error_count.split("+")[0]
    count=error_count.split("+")[1]
    print "  "+ip+":"+str(count)


