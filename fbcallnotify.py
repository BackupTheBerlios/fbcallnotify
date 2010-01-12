#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################
# Name: FBCallNotify
# Copyright (C): 2010 Maximilian Köhl
# License: GPLv3
#########################################

import ConfigParser
import os

from multiprocessmanager import Multiprocessmanager
from callmonitor import Callmonitor

print "License: GPLv3"
print "This program comes with ABSOLUTELY NO WARRANTY"

configpath=os.path.expanduser('~/.fbcallnotify/')

if not os.path.exists(configpath):
    os.mkdir(configpath)

mainconfig = ConfigParser.RawConfigParser()
mainconfig.read(configpath+'main.conf')

numberconfig = {}
i = 1
while i < mainconfig.getint('main', 'numbers') + 1:
    numberconfig[mainconfig.get('numbers', str(i))] = ConfigParser.RawConfigParser()
    numberconfig[mainconfig.get('numbers', str(i))].read(configpath+mainconfig.get('numbers', str(i))+'.conf')
    i = i + 1

multiprocessmanager = Multiprocessmanager()
callmonitor = Callmonitor(multiprocessmanager, numberconfig)

multiprocessmanager.addProcess(callmonitor.start, (mainconfig.get('main', 'host'), mainconfig.getint('main', 'port')))
multiprocessmanager.mainLoop()
