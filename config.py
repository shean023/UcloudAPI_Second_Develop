#-*- encoding: utf-8 -*-
import redis
import time

#配置公私钥"""
public_key  = " "
private_key = " "

base_url    = "http://api.ucloud.cn"

#redis db=0 is uhost,db=1 is mysql
ruhost = redis.Redis(host = '172.16.104.111', port = '6379', db=0)
rmysql = redis.Redis(host = '172.16.104.111', port = '6379', db=1)
rwarning = redis.Redis(host = '172.16.104.111', port = '6379', db=2)

timeStamp = int(time.time())
timeArray = time.localtime(timeStamp)
nowTime = time.strftime("%Y%m%d%H%M%S", timeArray)


#北京BGP3数据中心主机名和资源ID
cn_north_03_host={
    "www":" ",
    "pre":" ",
    "shop":" ",
    "picture":" ",
    "shop-admin":" ",
    "Shop-clodbackup":" ",
    "DRP":" "
    
    }

#华东数据中心uhost主机名和资源ID
cn_east_01_host={
    "www_coldbackup":" "
    
    }

#数据中心设置
DataCenter={
     "cn-north-03":cn_north_03_host,
     "cn-east-01":cn_east_01_host

    }
