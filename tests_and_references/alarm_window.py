import tkinter as t
import os
import platform
import pexpect


def run_again():
    os.system('python3 alarm_popup.py 1 --message="Take_a_break_and_refresh"')


def sleep_pc():
    if platform.system() == "Windows":
        try:
            os.system('echo "PC going to sleep now.."')
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        except OSError:
            os.system('''%windir%\System32\rundll32.exe powrprof.dll,SetSuspendState Hibernate''')
            exit(0)
            run_again()
    # for ubuntu..
    elif platform.system() == "Linux":
        try:
            sleep_child = pexpect.spawn('sudo systemctl suspend')
            sleep_child.expect('password')
            sleep_child.sendline('Chetu@123')
            print(sleep_child.read())
            print('System is going to sleep now...')
            root.destroy()
            run_again()
        except KeyboardInterrupt:
            print('Interrupted by user...')
        exit(0)


root = t.Tk()
root.config(bg='white')
root.geometry("450x120+1100+580")
alm_lbl = t.Label(root, text="\nRule no. 10:\nTime to leave desk for a couple of minutes.")
alm_lbl.config(bg='white', font=('Calibri', 13))
alm_lbl.pack()
sleep_button = t.Button(root, text="Sleep", command=sleep_pc).pack(side='left', padx=5, pady=5)
exit_button = t.Button(root, text="Exit", command=exit).pack(side='right', padx=5, pady=5)
root.mainloop()
