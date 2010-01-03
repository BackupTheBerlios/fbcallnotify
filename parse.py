# -*- coding:utf-8 -*-

import threading

import notifyer
 
class Parse(threading.Thread):
    def __init__(self, jobQueue):
        threading.Thread.__init__(self)
        self.jobQueue = jobQueue
        self.connections = {}
        self.events = {"RING" : self.on_ring,\
                            "CALL" : self.on_call,\
                            "CONNECT" : self.on_connect,\
                            "DISCONNECT" : self.on_disconnect}
        self.exit = False
        
    def setExit(self):
        self.exit = True
        
    def run(self):
        while True:
            info = self.jobQueue.get()
            if info != None:
                if info[1] in self.events:
                    self.events[info[1]](info)
                else:
                    print("Protokoll Error")
                    print(info)
            if self.exit:
                break

    def on_ring(self, info):
        self.connections[info[2]] = {'type':'in',\
                                        'from':info[3],\
                                        'to':info[4],\
                                        'overext':info[5],\
                                        'status':'off'}
        threading.Thread(target=notifyer.notifyer,args=[self.connections[info[2]]]).start()
                                    
    def on_call(self, info):
        self.connections[info[2]] = {'type':'out',\
                                        'from':info[4],\
                                        'to':info[5],\
                                        'overint':info[3]}
        threading.Thread(target=notifyer.notifyer,args=[self.connections[info[2]]]).start()
                    
    def on_connect(self, info):
        self.connections[info[2]]['status'] = 'on'
        self.connections[info[2]]['overint'] = info[3]
        threading.Thread(target=notifyer.notifyer,args=[self.connections[info[2]]]).start()
                    
    def on_disconnect(self, info):
        self.connections[info[2]]['status'] = 'off'
        self.connections[info[2]]['time'] = info[3]
        threading.Thread(target=notifyer.notifyer,args=[self.connections[info[2]]]).start()
                                                            

            
                    
