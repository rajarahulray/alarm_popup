import tkinter as t

root = t.Tk();
root.config(bg = 'white');
root.geometry("450x80+1100+580");
alm_lbl = t.Label(root, text = "\nRule no. 10:\nTime to leave desk for a couple of minutes.")
alm_lbl.config(bg = 'white',font = ('Calibri', 13));
alm_lbl.pack();
root.mainloop();
