'''A program to set an alarm notification for the time specified...'''

import time 
import tkinter as t
import sys
import os
import time

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
    root.title("Programmer_Alarm");
    root.config(bg = 'white');
    root.attributes('-topmost', True);
    root.geometry("450x80+1100+580");
    alm_lbl = t.Label(root, text = "\nRule no. 10:\nTime to leave desk for a couple of minutes.")
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
        cur_time = str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5]) ;
        print("Current Time - {}".format(cur_time));
        print("Setting an alarm for {} {}".format(mit, unt));
        time.sleep(sec);    
        alm_wdw();
    cur_time = str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5]) ;
    print("Alarm switched off at : {}".format(cur_time));
    print("Exiting Aplication...");

    slp = input("Do you want the system to sleep? (y/n)");

    #going to sleep mode...
    if slp == 'y':
        ##for windows..
        if os.environ['OS'] == "Windows_NT":
            os.system('echo "PC going to sleep now.."');
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            
        ##for ubuntu..
        else:
            os.system('echo "PC is going to sleep now.."')
            os.system('sudo systemctl suspend');
    else:
        exit(0);

except KeyboardInterrupt:
          print("Interupted by user..");
          sys.exit(1);

    
    
    

