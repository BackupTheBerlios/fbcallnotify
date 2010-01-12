# -*- coding:utf-8 -*-
#########################################
# Name: FBCallNotify
# Copyright (C): 2010 Maximilian Köhl
# License: GPLv3
#########################################

from multiprocessing import Process

class Multiprocessmanager():
    def __init__(self):
        self.processes = []
        
    def addProcess(self, function, args = ()):
        process = Process(target=function, args=args)
        process.start()
        self.processes.append(process)

    def mainLoop(self):
        for process in self.processes:
            process.join()    
