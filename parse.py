# -*- coding:utf-8 -*-

import threading
import random

from notifyer import Notifyer
 
class Parse(threading.Thread):
    def __init__(self,pool):
        threading.Thread.__init__(self)
        self.pool = pool
        self.connections = {}
        self.notifyer = {}
        
    def run(self):
        while True:
            info = self.pool.get()
            if info !=  None:           
                if info[1] == "RING":
                    self.connections[info[2]] = {'type':'in',\
                                                'from':info[3],\
                                                'to':info[4],\
                                                'overext':info[5],\
                                                'status':'off'}
                    randomid = random.randint(1000000000, 9999999999)
                    self.notifyer[randomid] = Notifyer(self.connections[info[2]])
                    self.notifyer[randomid].start()
                                    
                elif info[1] == "CALL":
                    self.connections[info[2]] = {'type':'out',\
                                                'from':info[4],\
                                                'to':info[5],\
                                                'overint':info[3]}
                    randomid = random.randint(1000000000, 9999999999)
                    self.notifyer[randomid] = Notifyer(self.connections[info[2]])
                    self.notifyer[randomid].start()
                    
                elif info[1] == "CONNECT":
                    self.connections[info[2]]['status'] = 'on'
                    self.connections[info[2]]['overint'] = info[3]
                    randomid = random.randint(1000000000, 9999999999)
                    self.notifyer[randomid] = Notifyer(self.connections[info[2]])
                    self.notifyer[randomid].start()
                    
                elif info[1] == "DISCONNECT":
                    self.connections[info[2]]['status'] = 'off'
                    self.connections[info[2]]['time'] = info[3]
                    randomid = random.randint(1000000000, 9999999999)
                    self.notifyer[randomid] = Notifyer(self.connections[info[2]])
                    self.notifyer[randomid].start()
                                        
                else:
                    print "Protokoll Error"
                    print info
            
                    
