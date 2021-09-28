from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
import threading as th
import pygame as pg
import gtts as gt
import time
import sys

#import self made modules/codes
import voice_temp
import apps_temp
import comp_temp



count = 0
lang='en'
textpath = 'files/maintext.txt'
txt = ''
x = pg.mixer.init()


def main():

    color='#42cbf5'

    root = Tk()
    root.geometry('400x400')
    root.title('Voice Update')
    root.config(bg=color)
    root.resizable(0,0)

    

    def restart(e=None):
        root.destroy()
        main()



#-----------------AUDIO TEMP---------------------

    

    def start(e=None):
        def s2():
            maintext = voice_temp.textload()
            battery = 'battery is at'+str(comp_temp.battery_percentage()) + 'percentage'

            th.Thread(target = voice_temp.startta(maintext, battery)).start()
            th.Thread(target = runall).start()
            time.sleep(2)
            comp_temp.start_music()

            time.sleep(10)
            sys.exit()
        th.Thread(target=s2).start()






#--------------APP TEMP------------------
    def runapp(e=None):
        apps_temp.run_apps()

    def runlink(e=None):
        apps_temp.run_links()

    def runall(e=None):
        runapp()
        runlink()

    img = PhotoImage(file='icon/mic.png')
    micbtn = Button(root, bd=0, image=img, bg=color, cursor='hand2', activebackground=color, command=start)
    micbtn.image=img
    micbtn.pack(pady=60)

    Button(root, bg='white', bd=0, cursor='hand2', text='Start', activebackground='black',
    activeforeground='white', height=2, command=start).pack(side=BOTTOM, padx=1, fill=X)





#----------------MENU-----------------------


    menu = Menu(root)
    root.config(menu=menu)
    file = Menu(menu, tearoff=0)
    menu.add_cascade(label='File', menu=file)
    file.add_command(label='Start', command=start)
    file.add_separator()
    file.add_command(label='Start Music', command=comp_temp.start_music)
    file.add_separator()
    file.add_command(label='Restart App', command=restart)
    file.add_command(label='Exit App', command=root.destroy)

    appman = Menu(menu, tearoff=0)
    menu.add_cascade(label='Manage Apps', menu=appman)
    appman.add_command(label='Run Apps & links', command=runall)
    appman.add_command(label='Run Apps', command=runapp)
    appman.add_command(label='Run Links', command=runlink)
    appman.add_separator()
    appman.add_command(label='Add Apps', command=apps_temp.add_apps)
    appman.add_command(label='Add Links', command=apps_temp.add_links)




    mainloop()



main()