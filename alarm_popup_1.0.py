"""
A program to set an alarm notification for the time specified...
Place our system password in config.py file
"""

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import sys
import os
import time
import platform
import pexpect
from config import config_dict

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

msg = ''


def check_command():
    trm = sys.argv
    len_trm = len(trm)
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
            global msg
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

    except KeyboardInterrupt:
        print("Interrupted by user..")
        sys.exit(1)


def exit_program():
    cur_time = str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5])
    print("Alarm switched off at : {}".format(cur_time))
    exit(0)


def run_again():
    os.system('python3 alarm_popup_1.0.py 1 --message="Take_a_break_and_refresh"')


def sleep_pc():
    if platform.system() == "Windows":
        try:
            os.system('echo "PC going to sleep now.."')
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        except OSError:
            os.system('''%windir%\System32\rundll32.exe powrprof.dll,SetSuspendState Hibernate''')
            cur_time = str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5])
            print("Alarm switched off at : {}".format(cur_time))
            exit(0)
            run_again()
    # for ubuntu..
    elif platform.system() == "Linux":
        try:
            sleep_child = pexpect.spawn('sudo systemctl suspend')
            sleep_child.expect('password')
            sleep_child.sendline(config_dict['system_password'])
            print(sleep_child.read())
            cur_time = str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5])
            print("Alarm switched off at : {}".format(cur_time))
            print('System is going to sleep now...')
            root.destroy()
            run_again()
        except KeyboardInterrupt:
            print('Interrupted by user...')
        exit(0)


check_command()

root = tk.Tk()
root.config(bg='white')
root.geometry("450x150+1100+580")
alm_lbl = tk.Label(root,
                   text="\nRule no. 10:\nTime to leave desk for a couple of minutes.\n{0}".format(msg))
alm_lbl.config(bg='white', font=('Calibri', 13))
alm_lbl.pack()
sleep_button = tk.Button(root, text="Sleep", command=sleep_pc).pack(side='left', padx=5, pady=5)
exit_button = tk.Button(root, text="Exit", command=exit_program).pack(side='right', padx=5, pady=5)
root.mainloop()
