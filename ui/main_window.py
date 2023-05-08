import tkinter
from .components import container

main_window = tkinter.Tk()


def get_screen_size():
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    return (screen_width, screen_height)


def initial_center(screen_width, screen_height, window_width, window_height):
    width_start = (screen_width / 2) - (window_width / 2)
    height_start = (screen_height / 2) - (window_height / 2)
    return width_start, height_start


def get_geometry(width, height):
    screen_width, screen_height = get_screen_size()
    width_window_start, height_window_start = initial_center(
        screen_width, screen_height, width, height
    )
    window_geometry = f'{width}x{height}+{int(width_window_start)}+{int(height_window_start)}'
    return window_geometry


def start():
    main_window.title("NetZer")
    # main_window.state('zoomed')
    window_width, window_height = get_screen_size()
    main_window.minsize((window_width-200), (window_height-200))
    main_window.configure(background='#11151c')
    container.start(main_window)
    # main_window.iconbitmap('ui/img/icons/icon.ico')
    main_window.mainloop()
