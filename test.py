#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdk import UcloudApiClient
from config import *
import sys
import json
import time

#实例化 API 句柄
'''
ResrouceType:uhost
Name 	          Description 	Unit
CPUUtilization 	   CPU使用率 	%
IORead 	           磁盘读流量 	B/s
IOWrite 	   磁盘写流量 	B/s
DiskReadOps        磁盘读次数 	次/s
DiskWriteOps       磁盘写次数 	次/s
NICIn 	           网卡入带宽 	b/s
NICOut 	           网卡出带宽 	b/s
NetPacketIn        网卡入包量 	个/s
NetPacketOut 	   网卡出包量 	个/s
MemUsage 	   内存使用率 	%
RootSpaceUsage 	   系统盘使用率 	%
DataSpaceUsage 	   数据盘使用率 	%
ReadonlyDiskCount 	只读磁盘个数 	个
RunnableProcessCount 	运行进程数量 	个
BlockProcessCount 	阻塞进程数量 	个

'''




#dck is datacenter, dcv is uhostname and sourceID
# print exzample  cn-east-01:{'www_coldbackup': 'uhost-cp2v41'}

for dck, dcv in DataCenter.iteritems():

    # k is uhostname v is source ID
    for k, v in dcv.items():

        
            arg_length = len(sys.argv)
            ApiClient = UcloudApiClient(base_url, public_key, private_key)
            Parameters={
                    "ResourceType":"uhost",
                    "ResourceId":v,
                    "TimeRange":"180",
                    "Action":"GetMetric",
                    "Region":dck,
                    "MetricName.0":"CPUUtilization",
                    "MetricName.1":"MemUsage",
                    "MetricName.2":"RootSpaceUsage",
                    "MetricName.3":"DataSpaceUsage",
                    "MetricName.4":"NICOut",
                    "MetricName.5":"RunnableProcessCount",
                    "MetricName.6":"BlockProcessCount",
                    "MetricName.7":"NICIn",

                    #"Period":"300"
                    }
            print '=============Start================'
            print 'uhost: %s' %(k)
            print
            response = ApiClient.get("/", Parameters );
          #  ApiClient.
            print response
            output = json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
            reson = json.loads(output)
            print reson
