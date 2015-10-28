#!/usr/bin/env python
#-*- coding: utf-8 -*-

import xinge
import json


def BuildNotification():
    msg = xinge.Message()
    msg.type = xinge.Message.TYPE_NOTIFICATION
    msg.title = 'title'
    msg.content = 'test'
    msg.expireTime = 86400
    style = xinge.Style(2, 1, 1, 0, 0)
    msg.style = style

    return msg


def DemoPushToken(x, msg):
    ret = x.PushSingleDevice(' ', msg, xinge.XingeApp.ENV_DEV)
    print ret

if '__main__' == __name__:
   
    x = xinge.XingeApp(2100150240, ' ')  #请输入手机TOKEN
    msg = BuildNotification()
    DemoPushToken(x, msg)
