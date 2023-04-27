from tkinter import *
from PIL import Image, ImageTk
import os
import tkinter

SIDE_MENU_WIDTH = 150
SIDE_MENU_BACKGROUND_COLOR = '#212d40'
BUTTON_BACKGROUND_COLOR = '#364156'
BUTTON_FONT_COLOR = '#ffffff'
ICON_SIZE = 40


def get_icon(icon_name, extension):
    icon_url = os.path.join(os.getcwd(), 'ui', 'img',
                            'icons', icon_name, f'.{extension}')
    return icon_url


def menu_button(frame, icon, text='', command=None):
    return Button(frame, image=icon, text=text, bg=BUTTON_BACKGROUND_COLOR, relief='flat', font=(0, 15), fg=BUTTON_FONT_COLOR, width=(int(SIDE_MENU_WIDTH*0.09)), height=2, command=command)


def menu_icon(icon_url):
    return ImageTk.PhotoImage(Image.open(icon_url).resize((ICON_SIZE, ICON_SIZE), Image.ANTIALIAS))


def start(window, notebook, network_tab, host_tab, home_tab):
    # icon1 = menu_icon(icon_url='ui/img/icons/home.png')
    # icon2 = menu_icon(icon_url='ui/img/icons/network.png')
    # icon3 = menu_icon(icon_url='ui/img/icons/host.png')

    window.update()
    side_menu = tkinter.Frame(window, bg=SIDE_MENU_BACKGROUND_COLOR,
                              width=SIDE_MENU_WIDTH, height=window.winfo_height())
    side_menu.pack(side='left', fill='y')

    button1 = menu_button(frame=side_menu, text='Home', icon='',
                          command=lambda: notebook.select(home_tab))
    button2 = menu_button(frame=side_menu, text='Network', icon='',
                          command=lambda: notebook.select(network_tab))
    button3 = menu_button(frame=side_menu, text='Host', icon='',
                          command=lambda: notebook.select(host_tab))

    button1.pack(side='top', padx=10, pady=10)
    button2.pack(side='top', padx=10, pady=10)
    button3.pack(side='top', padx=10, pady=10)

    side_menu.pack_propagate(False)
