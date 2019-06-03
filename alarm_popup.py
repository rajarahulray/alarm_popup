"""
A program to set an alarm notification for the time specified...
"""

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import sys
import os
import time
import platform

"""
Abbreviations :
1. trm : terminal
2. len_trm : length of terminal
3. minute : minute (min is a keyword)
4. sec : seconds
5. unit : unit (specifying unit for time.)
6. alm_wdw : alarm window
7. alm_lbl = alarm Label
8. msg = message defined by user..
"""


def alm_wdw():
    root = tk.Tk()
    root.title("Programmer_Alarm")
    root.config(bg='white')
    root.attributes('-topmost', True)
    root.geometry("450x150+1100+580")
    alm_lbl = tk.Label(root, text="\nRule no. 10:\nTime to leave desk for a couple of minutes.\n\n{}".format(msg))
    alm_lbl.config(bg='white', font=('Times New Roman', 15))
    alm_lbl.pack()
    root.mainloop()


trm = sys.argv
len_trm = len(trm)
msg = " "

if len_trm < 2:
    print("Please pass the time to set an alarm for and then your message(--message='<message>')(optional)")
    sys.exit(0)

# check for correct syntax for message...(only for now...)
elif len_trm > 3:
    print("Please use underscore to separate words in the message...")
    exit(0)

# check for user-defined message...
elif len_trm == 3:
    if trm[2].find('--message') != -1:
        msg = trm[2][trm[2].find("=") + 1:]
minute = ''
try:
    minute = int(trm[1])

except ValueError:
    print("Enter a numeric value > 0")

if minute < 0:
    print("Please specify a value > 0 for an alarm to set.")
    sys.exit(1)

sec = minute * 60

if minute == 1:
    unit = 'Min.'
else:
    unit = "Mins."

try:
    if minute > 0:
        cur_time = str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5])
        print("Current Time - {}".format(cur_time))
        print("Setting an alarm for {} {}".format(minute, unit))
        time.sleep(sec)
        alm_wdw()
    cur_time = str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5])
    print("Alarm switched off at : {}".format(cur_time))
    print("Exiting Application...")

    # raw_input()..in case user is using Python2.7
    try:
        slp = input("Do you want the system to sleep? (y/n)")
    except NameError:
        print("You are using Python2.x. Please Upgrade to Python3.x.")
        slp = raw_input("Do you want the system to sleep? (y/n)")

    # going to sleep mode...
    try:
        if slp == 'y' or slp == 'Y':
            # for windows..
            if platform.system() == "Windows":
                try:
                    os.system('echo "PC going to sleep now.."')
                    os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
                except OSError:
                    os.system('''%windir%\System32\rundll32.exe powrprof.dll,SetSuspendState Hibernate''')
            # for ubuntu..
            elif platform.system() == "Linux":
                os.system('sudo systemctl suspend')
                os.system('echo "PC is going to sleep now.."')
        elif slp == 'n' or slp == 'N':
            exit(0)

    except Exception as e:
        print(str(e))


except KeyboardInterrupt:
    print("Interrupted by user..")
    sys.exit(1)
