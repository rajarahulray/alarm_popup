'''A program to set an alarm notification for the time specified...'''

import time 
import tkinter as t
import sys

'''Abbrevations :
1. trm : terminal
2. len_trm : length of terminal
3. mit : minute (min is a keyword)
4. sec : seconds
5. unt : unit (specifying unit for time.)
6. alm_wdw : alarm window
7. alm_lbl = alarm Label
'''

def alm_wdw():
    root = t.Tk();
    root.config(bg = 'white');
    root.geometry("450x80+1100+580");
    alm_lbl = t.Label(root, text = "Rule no. 10:\nTime to leave desk for a couple of minutes.")
    alm_lbl.config(bg = 'white',font = ('Calibri', 13));
    alm_lbl.pack();
    root.mainloop();

trm = sys.argv;
len_trm = len(trm);

if len_trm != 2:
    print("Please pass the time to set an alarm for");
    sys.exit(0);

try:
    mit = int(trm[1]);

except ValueError:
    print("Enter a numeric value > 0");

if mit < 0:
    print("Please specify a value > 0 for an alarm to set.");
    sys.exit(1);

sec = mit * 60;

if mit == 1:
    unt = 'Min.';
else:
    unt = "Mins.";

try:
    if mit > 0:
        print("Setting an alarm for {} {}".format(mit, unt));
        time.sleep(sec);
        alm_wdw();
    
    print("Exiting Aplication...");
    sys.exit(1);

except KeyboardInterrupt:
          print("Interupted by user..");
          sys.exit(1);

    
    
    

