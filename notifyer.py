# -*- coding:utf-8 -*-

import threading
import random

from notify import Notify
from notify import Notify_Thread

class Notifyer(threading.Thread):
    def __init__(self, infos):
        threading.Thread.__init__(self)        
        self.infos = infos
        self.notify = {}
    
    def run(self):
        randomid = random.randint(1000000000, 9999999999)
        self.notify[randomid] = Notify("bash", self.infos)
        randomid = random.randint(1000000000, 9999999999)
        self.notify[randomid] = Notify_Thread("bash", self.infos)
        self.notify[randomid].start()
