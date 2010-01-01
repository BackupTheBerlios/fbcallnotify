#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import asyncore
import Queue

from callmonitor import Callmonitor
from parse import Parse

def genrandomid():
	randomid={}
	randomid[1]=random.randint(10000,99999)
	randomid[2]=random.randint(10000,99999)
	return randomid[1]+randomid[2]

ParseJobQueue = Queue.Queue(0)

callmonitor = Callmonitor("192.168.178.25",1030, ParseJobQueue)
parse = Parse(ParseJobQueue)
parse.start()

asyncore.loop()
