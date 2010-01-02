#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import asyncore
import Queue

from callmonitor import Callmonitor
from parse import Parse

ParseJobQueue = Queue.Queue(0)

callmonitor = Callmonitor("127.0.0.1", 1030, ParseJobQueue)
parse = Parse(ParseJobQueue)
parse.start()

asyncore.loop()
