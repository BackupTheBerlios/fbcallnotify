# -*- coding:utf-8 -*-
#########################################
# Name: FBCallNotify
# Copyright (C): 2010 Maximilian Köhl
# License: GPLv3
#########################################

import socket

import notifyer

class Callmonitor():
    def __init__(self, multiprocessmanager, numberconfig):
        self.processmanager = multiprocessmanager
        self.numberconfig = numberconfig
        self.connections = {}
        self.events = {'RING' : self.on_ring,\
                    'CALL' : self.on_call,\
                    'CONNECT' : self.on_connect,\
                    'DISCONNECT' : self.on_disconnect}

    def start(self, host, port):
        try:
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.connect((host, port))
            tmpdata = ''
            while True:
                data = self.connection.recv(1024)
                tmpdata += data
                if data:
                    if tmpdata.endswith('\n'):
                        for infostr in (tmpdata.split('\n')):
                            info = infostr.split(';')
                            if info[0]:
                                if info[1] in self.events:
                                    self.events[info[1]](info)
                                else:
                                    print('Protokoll Error')
                                    print(info)
                        tmpdata = ''
                else:
                    print 'Connection closed...'
                    break
            self.connection.close()
        except:
            print 'Can\'t create socket...'     
    
    def on_ring(self, info):
        self.connections[info[2]] = {'type':'in',\
                                        'from':info[3],\
                                        'to':info[4],\
                                        'overext':info[5],\
                                        'status':'off',\
                                        'number':info[4]}
        if self.connections[info[2]]['number'] in self.numberconfig:
            self.processmanager.addProcess(notifyer.notifyer, args=[self.connections[info[2]], self.numberconfig[self.connections[info[2]]['number']], 'ring'])                                    
    def on_call(self, info):
        self.connections[info[2]] = {'type' : 'out',\
                                        'from' : info[4],\
                                        'to' : info[5],\
                                        'overint' : info[3],\
                                        'status' : 'off',\
                                        'number' : info[4]}
        if self.connections[info[2]]['number'] in self.numberconfig:
            self.processmanager.addProcess(notifyer.notifyer, args=[self.connections[info[2]], self.numberconfig[self.connections[info[2]]['number']], 'call']) 
                    
    def on_connect(self, info):
        self.connections[info[2]]['status'] = 'on'
        self.connections[info[2]]['overint'] = info[3]
        if self.connections[info[2]]['number'] in self.numberconfig:
            self.processmanager.addProcess(notifyer.notifyer, args=[self.connections[info[2]], self.numberconfig[self.connections[info[2]]['number']], 'connect']) 
                    
    def on_disconnect(self, info):
        self.connections[info[2]]['status'] = 'off'
        self.connections[info[2]]['time'] = info[3]
        if self.connections[info[2]]['number'] in self.numberconfig:
            self.processmanager.addProcess(notifyer.notifyer, args=[self.connections[info[2]], self.numberconfig[self.connections[info[2]]['number']], 'disconnect']) 


