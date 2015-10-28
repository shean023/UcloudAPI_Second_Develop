#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdk import UcloudApiClient
from config  import *
import sys
import json

for dck,dcv in DataCenter.iteritems():

    for k, v in dcv.items():
        
        if __name__=='__main__':
            arg_length = len(sys.argv)
            ApiClient = UcloudApiClient(base_url, public_key, private_key)
            
            Parameters={
                
                "Action":"CreateCustomImage",
                "UHostId":v,
                "ImageName":k+nowTime,
                "Region":dck
                
                }
            
            response = ApiClient.get("/", Parameters);
            print response;
            time.sleep(3)
            print
print 'Backup Finish!'
