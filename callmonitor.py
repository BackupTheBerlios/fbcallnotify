# -*- coding:utf-8 -*-

import socket
import asyncore
import threading

class Callmonitor(asyncore.dispatcher):
    def __init__(self, host, port, jobQueue):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        
        self.host = host
        self.port = port
        self.jobQueue = jobQueue
        self.exit = False
        
        self.asyncoreThread = threading.Thread(target=self.check).start()
         
        print "Connected to %s:%d" % (host,port)
   
    def setExit(self):
        self.exit = True
   
    def handle_connect(self):
        pass
        
    def handle_read(self):
        tmpinfo = ""
        while True:
            tmpinfo += self.recv(8192)
            if tmpinfo.endswith("\n"):
                for infostr in (tmpinfo.split('/n')):
                    info = infostr.split(';')
                    if info[0]:
                        self.jobQueue.put(info)
                break
    
    def handle_close(self):
        print "Disconnected"
        self.close()
    
    def writable(self):
        return False

    def check(self):
        while True:
            asyncore.poll()
            if self.exit:
                break
