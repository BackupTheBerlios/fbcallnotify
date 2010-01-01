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
		randomid = genrandomid()
		self.notify[randomid] = notify("bash", self.infos)
		randomid = genrandomid()
		self.notify[randomid] = notify_thread("bash", self.infos)
		self.notify[randomid].start()
