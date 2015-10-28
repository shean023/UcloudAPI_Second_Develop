#!/usr/bin/env python
#-*- coding: utf-8 -*-

from sdk import UcloudApiClient
from config import *
import sys
import json
import time

#实例化 API 句柄
'''
Name 	      Description 	Unit
CPUUtilization 	CPU使用率 	%
MemSize 	内存大小   	MB
MemUsage 	内存使用率 	%
ConnectionCount 连接数     	个/s
QPS 	        请求数     	个/s
DeleteQPS 	删除请求数 	个/s
InsertQPS 	插入请求数 	个/s
SelectQPS 	查询请求数 	个/s
UpdateQPS 	更新请求数 	个/s
'''

if __name__=='__main__':
    arg_length = len(sys.argv)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters={
            "ResourceType":"udb",
            "ResourceId":"udb-jemy01",
            "TimeRange":"300",
            "Action":"GetMetric",
            "Region":"cn-north-03",
            "MetricName.0":"CPUUtilization",
            "MetricName.1":"MemUsage",
            "MetricName.2":"ConnectionCount",
            "MetricName.3":"QPS",
            "MetricName.4":"DeleteQPS",
            "MetricName.5":"InsertQPS",
            "MetricName.6":"SelectQPS",
            "MetricName.7":"UpdateQPS",
            "MetricName.8":"MemSize",

           # "Period":"180"
            }
    response = ApiClient.get("/", Parameters )
    output = json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
    reson = json.loads(output)
    x = reson.get('DataSets')
    print


    
    for item, value in x.items():
             try:
                 a = value[0]
                 ltime=time.localtime(a['Timestamp'])
                 print '%s\t%s\t%s' %( time.strftime("%Y%m%d%H%M%S", ltime), a['Value'], item)
                 rvalue = [ time.strftime("%Y%m%d%H%M%S", ltime) , a['Value'] ]
                 rmysql.set(item, rvalue)
                 rmysql.expire(item,360)
             except IndexError:
                 print item + " ," + "No Data Input pls try again!"
                 rvalue = [ '-1' , '-1' ]
                 print rvalue
                 rmysql.set(item, rvalue)
                 rmysql.expire(item, 360)
            


                 
