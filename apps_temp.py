import os
import webbrowser
from tkinter import filedialog
from tkinter import *

def run_apps(e=None):
    apps = []

    f = open('files/apps.txt', 'r')
    for line in f.readlines():
        line = line.strip('\n')
        apps.append(line)
    f.close()

    for item in apps:
        os.startfile(item)




def run_links(e=None):
    links = []

    f = open('files/links.txt', 'r')
    for line in f.readlines():
        line = line.strip('\n')
        links.append(line)
    f.close()

    for item in links:
        webbrowser.open_new_tab(item)


def add_apps(e=None):
    filename = filedialog.askopenfilename(title='Choose Application', defaultextension=(('EXE Files', '.exe')))

    apps = []

    f = open('files/apps.txt', 'r')
    for line in f.readlines():
        line = line.strip('\n')
        apps.append(line)
    f.close()
    apps.append(filename)

    
    f = open('files/apps.txt', 'w')
    for app in apps:
        f.write(app+'\n')
    f.close()


def add_links(e=None):
    win = Toplevel()
    win.title('Add Link')
    win.geometry('300x300')

    Label(win, text='Link:').pack(pady=3)
    linkentry = Entry(win, bd=1, width=30)
    linkentry.pack(pady=3)

    def sub():
        links = []

        f = open('files/links.txt', 'r')
        for line in f.readlines():
            line = line.strip('\n')
            links.append(line)
        f.close()
        links.append(linkentry.get())

        
        f = open('files/links.txt', 'w')
        for app in links:
            f.write(app+'\n')
        f.close()

        linkentry.delete(0, END)

    Button(win, text='Submit', bd=0, bg='blue', fg='white', command=sub).pack(pady=10)



def delete_apps(e=None):
    pass


def delete_links(e=None):
    pass
