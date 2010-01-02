# -*- coding:utf-8 -*-

import threading
import os

class Notify():
    def __init__(self, flag, data):
        if flag == "bash":
            print data
    
class Notify_Thread(threading.Thread):
    def __init__(self, flag, data):
        threading.Thread.__init__(self)
        self.flag = flag
        self.data = data
    
    def run(self):
        if self.flag == "bash":
            print self.data        
