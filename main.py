import datetime
import pygame
from tkinter import *

# colors
purple = '#80247f'
turquoise = '#005f64'
white = '#fff'


pygame.init()
sound = pygame.mixer.Sound('sound/sound.wav')

main_font = 'Arial'

window = Tk()
window.geometry('300x150')
window.config(bg=purple)
window.iconbitmap('icon/icon2.ico')
window.title('Alarm clock')



# funkce tlacitek
def sound_play():   
    sound.play()

def sound_stop():
    sound.stop()


# funkce labelu cas
def get_current_time():
    actuell_time = datetime.datetime.now()
    return actuell_time.strftime("%H:%M:%S")

def update_time():
    actuel_time = get_current_time()
    current_time.config(text=actuel_time) 
    window.after(1000, update_time)

# funkce na zazvoneni

def user_input():
    hh = hours.get()
    mm = minutes.get()
    return f'{hh}:{mm}:00'


def time_compare():
    user = user_input()
    current = get_current_time()
    if user == current:
        sound_play()

# hlavni smycka 

def update_time_compare():
    time_compare()
    window.after(1000, update_time_compare)

# funkce pro snooze
def snooze_button():
    sound_stop()
    snooze_time = (datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime("%H:%M:%S")
    hours.delete(0, END)
    hours.insert(0, snooze_time[:2])
    minutes.delete(0, END)
    minutes.insert(0, snooze_time[3:5])

    
# aktualni cas
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



#!! vytvorit funkci na pripocitani 5 minut a spusteni znovu
button_snooze = Button(window, text='Snooze', command=snooze_button, bg=turquoise, fg=white, width=7)
button_snooze.place(x=190, y=30)

# vypnuti budiku
button_stop = Button(window, text='Stop', command=sound_stop, bg=turquoise, fg=white, width=7)
button_stop.place(x=190, y=80)


update_time()
update_time_compare()
window.mainloop()
pygame.quit()
