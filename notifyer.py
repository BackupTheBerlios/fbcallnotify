# -*- coding:utf-8 -*-
#########################################
# Name: FBCallNotify
# Copyright (C): 2010 Maximilian Köhl
# License: GPLv3
#########################################

import pynotify
import os
import subprocess

pynotify.init("FBCallNotify")

def notifyer(data, numberconfig, actiontype):
    events = {"print" : event_print,\
                "exec" : event_exec,\
                "libnotify" : event_libnotify}
                                        
    i = 1
    while i < numberconfig.getint(actiontype, 'number') + 1:
        if numberconfig.get(actiontype+str(i), 'type') == 'print':
            printstr = numberconfig.get(actiontype+str(i), 'str')
            events['print'](printstr, data)
        elif numberconfig.get(actiontype+str(i), 'type') == 'exec':
            command = numberconfig.get(actiontype+str(i), 'command')
            events['exec'](command, data)
        elif numberconfig.get(actiontype+str(i), 'type') == 'libnotify':
            title = numberconfig.get(actiontype+str(i), 'title')
            infostr = numberconfig.get(actiontype+str(i), 'str')
            events['libnotify'](title, infostr, data)
        i = i + 1
    
def data_replace(infostr, data):
    infostr = infostr.replace('%TYPE%', data['type'])
    infostr = infostr.replace('%FROMNUMBER%', data['from'])
    infostr = infostr.replace('%TONUMBER%', data['to'])
    if 'overext' in data:
        infostr = infostr.replace('%OVEREXT%', data['overext'])
    if 'overint' in data:
        infostr = infostr.replace('%OVERINT%', data['overint'])
    if 'time' in data:
        infostr = infostr.replace('%TIME%', data['time'])
    infostr = infostr.replace('%STATUS%', data['status'])   
    return infostr

def event_print(printstr, data):
    print data_replace(printstr, data)
    
def event_libnotify(title, infostr, data):
    title = data_replace(title, data)
    infostr = data_replace(infostr, data)
    notify = pynotify.Notification(title, infostr)
    notify.show()
    
def event_exec(command, data):
    command = data_replace(command, data)
    process = subprocess.Popen(command, shell=True)
    process.wait()
