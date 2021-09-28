import psutil
import os
import shutil
import webbrowser
import time


def battery_percentage(e=None):
    bat = psutil.sensors_battery()
    battery = bat.percent
    return battery

def bat_charge(e=None):
    bat = psutil.sensors_battery()

def start_music(e=None):

    time.sleep(1)
    url = 'https://www.youtube.com/watch?v=D_QLxj8jCF0&list=PLHlXLRUvzi99vwpBBIbO_rKLTKiUBf9CE&index=1'
    webbrowser.open_new_tab(url)
    

