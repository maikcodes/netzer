from .forms import home, host, network, ports_list
from . import side_menu
from tkinter import ttk


def configure_container():
    notebook_style = ttk.Style()
    notebook_style.layout('TNotebook.Tab', [])
    notebook_style.theme_create(themename='dark_mode', settings={
        "TNotebook.Tab": {
            "configure": {'borderwidth': 0},
            "layout": [("Notebook.tab", {"sticky": "nswe"})],
        },
        "TNotebook": {
            "configure": {"borderwidth":0},
        }
    })
    notebook_style.theme_use('dark_mode')
# notebook_style.configure('TNotebook.Tab', padding=[0, 0], font=('TkDefaultFont', 0), borderwidth=0)

# notebook = ttk.Notebook(main_window, style='TNotebook')


def create_forms(notebook):
    home_tab = ttk.Frame(notebook)
    home.create_form_panel(home_tab)
    home.create_table_panel(home_tab)
    notebook.add(home_tab, text='Home')
    home.create(home_tab)

    network_tab = ttk.Frame(notebook)
    network.create_form_panel(network_tab)
    network.create_table_panel(network_tab)
    notebook.add(network_tab, text='Network')
    network.create(network_tab)

    host_tab = ttk.Frame(notebook)
    host.create_form_panel(host_tab)
    host.create_table_panel(host_tab)
    notebook.add(host_tab, text='Host')
    host.start(host_tab)

    ports_list_tab = ttk.Frame(notebook)
    ports_list.create_ports_list_table(ports_list_tab)
    notebook.add(ports_list_tab, text='Ports list')
    ports_list.create(ports_list_tab)

    return home_tab, network_tab, host_tab, ports_list_tab


def start(window):
    notebook = ttk.Notebook(window)
    configure_container()
    home_tab, network_tab, host_tab, ports_list_tab = create_forms(notebook)
    side_menu.start(window, notebook, network_tab,
                    host_tab, home_tab, ports_list_tab)
    notebook.pack(expand=True, fill='both')
