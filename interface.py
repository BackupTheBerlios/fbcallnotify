# -*- coding:utf-8 -*-

def start():
    print "FBCallNotify - Command Promt"
    while True:
        action = raw_input("Type \"help\" for help: ")
        if action == "exit":
            break
        elif action == "help":
            print "Hilfe"

