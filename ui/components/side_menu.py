from tkinter import *
import tkinter

SIDE_MENU_WIDTH = 150
SIDE_MENU_BACKGROUND_COLOR = '#121721'
BUTTON_BACKGROUND_COLOR = '#364156'
BUTTON_FONT_COLOR = '#ffffff'
ICON_SIZE = 40


def menu_button(frame, icon, text='', command=None):
    return Button(
        frame, image=icon, text=text, bg=BUTTON_BACKGROUND_COLOR,
        relief='flat', font=(0, 15), fg=BUTTON_FONT_COLOR,
        width=(int(SIDE_MENU_WIDTH*0.09)), height=2, command=command
    )


def start(window, notebook, tabs):
    network_tab = tabs['network']
    host_tab = tabs['host']
    ports_list_tab = tabs['ports_list']

    window.update()

    side_menu = tkinter.Frame(
        window, bg=SIDE_MENU_BACKGROUND_COLOR, width=SIDE_MENU_WIDTH, height=window.winfo_height()
    )
    side_menu.pack(side='left', fill='y')

    network_button = menu_button(
        frame=side_menu, text='Network', icon='', command=lambda: notebook.select(network_tab)
    )
    host_button = menu_button(
        frame=side_menu, text='Host', icon='', command=lambda: notebook.select(host_tab)
    )
    ports_button = menu_button(
        frame=side_menu, text='Ports list', icon='', command=lambda: notebook.select(ports_list_tab)
    )

    network_button.pack(side='top', padx=10, pady=10)
    host_button.pack(side='top', padx=10, pady=10)
    ports_button.pack(side='top', padx=10, pady=10)

    side_menu.pack_propagate(False)
