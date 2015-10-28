#!/usr/bin/env python
#-*- codeing: utf-8 -*-
import sys
import redis
import time
import xinge
import json
from  config import *


#ruhost = redis.Redis(host = '172.16.104.214', port = '6379', db=0)
#rmysql = redis.Redis(host = '172.16.104.214', port = '6379', db=1)
#rwarning = redis.Redis(host = '172.16.104.111', port = '6379', db=2)

udbMonitorArgs={

	"QPS":"200",
	"UpdateQPS":"100",
	"DeleteQPS":"100",
	"InsertQPS":"100",
	"SelectQPS":"100",
	"ConnectionCount":"50",
	"MemSize":"50", #MB
	"CPUUtilization":"100", #%
	"MemUsage":"80" #%

	}

uhostMonitorArgs={
    
    "CPUUtilization":"80",
    "MemUsage":"80",
    "NICIn":"2097152",
	"NICOut":"2097152",
	"RootSpaceUsage":"70",
	"DataSpaceUsage":"70",	
	"BlockProcessCount":"3",
	"RunnableProcessCount":"3",
	

	}

def BuildNotification():
		msg = xinge.Message()
		msg.type = xinge.Message.TYPE_NOTIFICATION
		msg.title = utitle
		msg.content = umsg
		msg.expireTime = 86400
		style = xinge.Style(2, 1, 1, 0, 0)
		msg.style = style

		return msg


def DemoPushToken(x, msg):
		ret = x.PushSingleDevice(' ', msg, xinge.XingeApp.ENV_DEV) #'Mobile Token No.'
		print ret

def RecoveryNotification(name,item):
    if rwarning.exists(name+item):
        rwarning.delete(name+item)
        msg = BuildNotification()
        DemoPushToken(x, msg)
    else:
        pass


def WarningNotification(name,item):
    if rwarning.exists(name+item):
        pass
    else:

        rwarning.set(name+item, 'Over Warning!')
        rwarning.expire(name+item,600)
        msg = BuildNotification()
        DemoPushToken(x, msg)


global utitle, umsg




def udbMonitor():
    global utitle, umsg

    print 'Mysql-Master'


    for item, value in udbMonitorArgs.items():

       try:

            if rmysql.exists(item):

                     udbargs =  eval(rmysql.get(item))
                     if (udbargs[1] != '-1'):
                             utitle = 'MySQL-Master OK'
                             umsg = udbargs[0] ,udbargs[1],'(' + value +')',item
                             if int(udbargs[1]) < int(value) and item != 'MemSize':
                                # pass
                                 RecoveryNotification('MySQL-Master',item)
                                 print 'OK', udbargs[0] ,udbargs[1], '(' + value +')',item

                             elif   item == 'MemSize' and int(udbargs[1]) > int(value):
                               #  pass
                                 RecoveryNotification('MySQL-Master',item)
                                 print 'OK', udbargs[0] ,udbargs[1], '(' + value +')',item

                             elif  item == 'MemSize' and int(udbargs[1]) < int(value):
                                 utitle = 'MySQL-Master Danger'
                                 print 'Error', '\33[91m' +  udbargs[0] ,udbargs[1], '(' + value +')', item + '\33[0m'
                                 WarningNotification('MySQL-Master',item)


                             else:
                                 print 'Error', '\33[91m' +  udbargs[0] ,udbargs[1], '(' + value +')', item + '\33[0m'
                                 utitle = 'MySQL-Master Danger'
                                 WarningNotification('MySQL-Master',item)


                     else:

                         print item + " ," + 'UcloudAPI Nodata Back!'

            else:


                 print  item + " ," + 'MySQL-Master NO Redis Data,Pls Check!'


       except IndexError:          
           print  item + " ," + "No Data Input, pls try again!"

    print

def uhostMonitor():
    global utitle, umsg
    for dc in DataCenter.values():
        for uhost in dc.keys():
            print
            print uhost
            for uhostitem, uhostvalue in uhostMonitorArgs.items():

                if ruhost.exists(uhost+uhostitem):
                    try:
                        uhostargs =  eval(ruhost.get(uhost+uhostitem))
                        # print uhostargs[0],uhostargs[1],uhostargs[2]
                        utitle = uhost+' '+ 'OK'
                        umsg = uhostargs[0], uhostargs[1], "(" + uhostvalue + ")", uhostargs[2]

                        if int(uhostargs[1]) != int(-1):
                            if int(uhostvalue) > int(uhostargs[1]):
                               # pass

                               print 'OK' + ' ' + uhostargs[0], uhostargs[1], '(' + uhostvalue +')', uhostargs[2]
                               RecoveryNotification(uhost,uhostargs[2])

                            else:

                                print 'Danger:'+ '\33[91m' + uhostargs[0], uhostargs[1], '(' + uhostvalue +')', uhostargs[2] + '\33[0m'
                                utitle = uhost+' '+ 'Danger'
                                WarningNotification(uhost,uhostargs[2])

                        else:
                            print '\33[91m' + 'Error:' + uhostargs[0], uhostargs[1], "(" + uhostvalue + ")", uhostargs[2] + '\33[0m'


                    except KeyError:

                        print 'KeyError'

                else:

                    print "No Data In Redis, Pls Check!"


if __name__=='__main__':

     x = xinge.XingeApp( , ' ')
     #while True:

     print '==========Start==========='
     udbMonitor()
     uhostMonitor()
     print '==========End============='
         #time.sleep(120)








