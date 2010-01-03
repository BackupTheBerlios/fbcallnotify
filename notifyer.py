# -*- coding:utf-8 -*-

import threading
import pynotify

def notifyer(data):
    events = {"print" : event_print,\
                "notify" : event_libnotify}
    events["print"](data)
    events["notify"]("FBCallNotify", data)
    # Thread
    threading.Thread(target=events["print"],args=[data]).start()
            
def event_print(data):
    print data
    
def event_libnotify(name, data):
    pynotify.init("FBCallNotify")
    notify = pynotify.Notification(name, str(data))
    notify.show()
