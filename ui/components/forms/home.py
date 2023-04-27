import tkinter as tk


def create_form_panel(parent):
    form_panel = tk.Frame(parent, bg='green', width=800, height=200)
    # Agrega aquí los widgets que conforman el formulario
    return form_panel


def create_table_panel(parent):
    table_panel = tk.Frame(parent, bg='red', width=800, height=100)
    # Agrega aquí la tabla o lista con los datos necesarios
    return table_panel


def create(tab):
    form_panel = create_form_panel(tab)
    table_panel = create_table_panel(tab)
    form_panel.pack(side='top', fill='x')
    table_panel.pack(side='bottom', fill='both', expand=True)

