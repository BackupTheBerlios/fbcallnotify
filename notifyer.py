# -*- coding:utf-8 -*-

import threading
import pynotify

def notifyer(data):
    events = {"print" : event_print,\
                "notify" : event_libnotify,\
                "exec" : event_exec}
    events["print"](data)
    events["notify"](data)
    # Thread
    threading.Thread(target=events["print"],args=[data]).start()
            
def event_print(data):
    print data
    
def event_libnotify(data):
    pynotify.init("FBCallNotify")
    notify = pynotify.Notification("Test", str(data))
    notify.show()

def event_exec(data):
    print "Exec"
