from .forms import home, host, network, ports_list
from . import side_menu
from tkinter import ttk


def configure_container():
    notebook_style = ttk.Style()
    notebook_style.layout('TNotebook.Tab', [])
    notebook_style.theme_create(
        themename='dark_mode', settings={
            "TNotebook.Tab": {
                "configure": {'borderwidth': 0},
                "layout": [("Notebook.tab", {"sticky": "nswe"})],
            },
            "TNotebook": {
                "configure": {"borderwidth": 0},
            }
        }
    )
    notebook_style.theme_use('dark_mode')


def create_forms(notebook):
    network_tab = ttk.Frame(notebook)
    network.create_form_panel(network_tab)
    network.create_table_panel(network_tab)
    notebook.add(network_tab, text='Network')
    network.start(network_tab)

    host_tab = ttk.Frame(notebook)
    host.create_form_panel(host_tab)
    host.create_table_panel(host_tab)
    notebook.add(host_tab, text='Host')
    host.start(host_tab)

    ports_list_tab = ttk.Frame(notebook)
    ports_list.create_ports_list_table(ports_list_tab)
    notebook.add(ports_list_tab, text='Ports list')
    ports_list.create(ports_list_tab)

    tabs = {
        'network': network_tab,
        'host': host_tab,
        'ports_list': ports_list_tab
    }

    return tabs


def start(window):
    notebook = ttk.Notebook(window)
    configure_container()
    tabs = create_forms(notebook)

    side_menu.start(window, notebook, tabs)
    notebook.pack(expand=True, fill='both')
