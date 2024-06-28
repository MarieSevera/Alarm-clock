import datetime
import pygame
from tkinter import *

# colors and font
purple = '#80247f'
turquoise = '#005f64'
white = '#fff'
main_font = 'Arial'

pygame.init()
sound = pygame.mixer.Sound('sound/sound.wav')

window = Tk()
window.geometry('280x140')
window.config(bg=purple)
window.iconbitmap('icon/icon2.ico')
window.title('Alarm clock')

# funkcions - sound
def sound_play():   
    sound.play()

def sound_stop():
    sound.stop()

# funkcions - time
def get_current_time():
    actuell_time = datetime.datetime.now()
    return actuell_time.strftime("%H:%M:%S")

def update_time():
    actuel_time = get_current_time()
    current_time.config(text=actuel_time) 
    window.after(1000, update_time)

# funkcion - time compare and ring
def user_input():
    hh = hours.get()
    mm = minutes.get()
    return f'{hh}:{mm}:00'

def time_compare():
    user = user_input()
    current = get_current_time()
    if user == current:
        sound_play()

# main loop
def update_time_compare():
    time_compare()
    window.after(1000, update_time_compare)

# snooze
def snooze_button():
    sound_stop()
    snooze_time = (datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime("%H:%M:%S")
    hours.delete(0, END)
    hours.insert(0, snooze_time[:2])
    minutes.delete(0, END)
    minutes.insert(0, snooze_time[3:5])

# Label - current time
current_time = Label(window, bg=purple, fg=white)
current_time.place(x= 70, y= 80)

# HH
hours = Entry(window, justify=CENTER, font=(main_font, 15), width=4)
hours.place(x=25, y=30)

# :
colon = Label(window, text=':', font=(main_font, 15), bg=purple, fg=white)
colon.place(x=85, y=30)

# MM
minutes = Entry(window, justify=CENTER, font=(main_font, 15), width=4)
minutes.place(x=105, y=30)

# Button - Snooze
button_snooze = Button(window, text='Snooze', command=snooze_button, bg=turquoise, fg=white, width=7)
button_snooze.place(x=190, y=30)

# Button - Stop
button_stop = Button(window, text='Stop', command=sound_stop, bg=turquoise, fg=white, width=7)
button_stop.place(x=190, y=80)

update_time()
update_time_compare()
window.mainloop()
pygame.quit()