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
        tmpinfo = ""
        while True:
            tmpinfo += self.recv(8192)
            if tmpinfo.endswith("\n"):
                for infostr in (tmpinfo.split('/n')):
                    info = infostr.split(';')
                    if info[0]:
                        self.jobQueue.put(info)
                break
            else:
                pass
    
    def handle_close(self):
        print "Disconnected"
        self.close()
    
    def writable(self):
        return False

            
