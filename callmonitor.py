# -*- coding:utf-8 -*-

import socket
import asyncore

class Callmonitor(asyncore.dispatcher):
	def __init__(self, host, port, jobQueue):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect((host, port))
		
		self.host = host
		self.port = port
		self.jobQueue = jobQueue
		
		print "Connected to %s:%d" % (host,port)
	
	def handle_connect(self):
		pass
		
	def handle_read(self):
		for infostr in (self.recv(8192).split('/n')):
			info = infostr.split(';')
			if info[0]:
				print info
				self.jobQueue.put(info)
	
	def handle_close(self):
		print "Disconnected"
		self.close()
	
	def writable(self):
		return False

			
