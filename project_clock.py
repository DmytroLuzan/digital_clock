from tkinter import *
from time import strftime


# Constants
window_width = 750
window_height= 450
bg_color = '#37474f'
fg_color = 'white'
color_h = '#00897b'
color_m = '#4A8FE7'
color_s = '#8e24aa'


def create_obj():
    s_x, s_y = 100, 100

    for i in range(3):
        label = Label(window, font=('Futura PT', 50), bg=color_h, fg=fg_color, text='13')
        label.place(x=s_x, y=s_y, width=150, height=150)
        s_x += 200
        label_clock.append(label)

    label_clock[1].config(bg=color_m)
    label_clock[2].config(bg=color_s)

    s_x, s_y = 100, 275

    for i in range(3):
        label = Label(window, font=('Futura PT', 25), bg=color_h, fg=fg_color, text='Clock')
        label.place(x=s_x, y=s_y, width=150, height=50)
        s_x += 200
        label_text.append(label)

    label_text[1].config(bg=color_m, text='minutes')
    label_text[2].config(bg=color_m, text='second')


def update_clock():
    h = strftime('%H')
    m = strftime('%M')
    s = strftime('%S')

    label_clock[0].config(text='{}'.format(h))
    label_clock[1].config(text='{}'.format(m))
    label_clock[2].config(text='{}'.format(s))

    window.after(1000, update_clock)
        
window = Tk()
window.title('Clock')
window.resizable(False, False)


canvas = Canvas(window, bg=bg_color, height=window_height, width=window_width)
canvas.place(x=0, y=0)


window.geometry('375x125')

label_clock = []
label_text = []

create_obj()
update_clock()

window.mainloop()
