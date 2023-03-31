# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:17:13 2016

@author: cbhattar
"""

import u3
#from time import gmtime, strftime
import datetime
import time, sys
d = u3.U3()
print (d.configU3())
stored_exception=None
fname=datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d_%H%M%S_')+'particleloss_UV.txt'
#fname=datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d_')+'labjack.txt'
x=1
file=open(fname, 'a')
file.write('Date,NO,NOx,UV,CO\n')
file.close()
while True:
    file=open(fname, 'a') 
    try:    
        #file.write('input \n')
        tstep=datetime.datetime.strftime(datetime.datetime.now(),"%Y%m%d %H:%M:%S")
        CO=d.getAIN(0)
        NOx=d.getAIN(1)
        UV=d.getAIN(3)
        NO=d.getAIN(2)
        print(tstep, UV)
        #file.write("%s,%2.5f,%2.5f,%2.5f,%2.5f\n" %(tstep,NO,NOx,UV,CO))
        file.write("%s,%2.5f\n" %(tstep,UV))
        time.sleep(1)
        #print("Press CTRL +C to break operation")
        file.close()
        if stored_exception:
              break
        x+=1
    except KeyboardInterrupt:
        print ("[CTRL+C detected]")
        stored_exception=sys.exc_info()
if stored_exception:
    raise (stored_exception[0], stored_exception[1], stored_exception[2])
sys.exit()
