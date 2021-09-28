import gtts as gt
import pygame as pg
import os
from tkinter import *
import time

count = 0
lang='en'
textpath = 'files/maintext.txt'
txt = ''



def textload():
    f = open(textpath, 'r')
    global txt
    txt = f.read()
    f.close()
    return txt


def startta(text, battery):
    def t():
        global count

        audio = gt.gTTS(text=text, lang=lang, slow=False)
        audio.save(f'audio/audio{count%2}.mp3')

        pg.mixer.music.load(f'audio/audio{count%2}.mp3')
        pg.mixer.music.play(loops=0)
        count +=1
        time.sleep(25)
        b()

    

    def b():

        global count
        audio = gt.gTTS(text=battery, lang=lang, slow=False)
        audio.save(f'audio/audio{count%2}.mp3')

        pg.mixer.music.load(f'audio/audio{count%2}.mp3')
        pg.mixer.music.play(loops=0)


        count +=1

    t()
