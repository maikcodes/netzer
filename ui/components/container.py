from .forms import host, network, ports_list
from . import side_menu
from tkinter import ttk


def configure_container():
    notebook_style = ttk.Style()
    notebook_style.layout('TNotebook.Tab', [])
    # crea un nuevo estilo para el contenedor (estilo de notebook)
    notebook_style.theme_create(
        # crea el tema especifico nombrado dark_mode y sus configuraciones
        themename='dark_mode', settings={
            "TNotebook.Tab": {
                "configure": {'borderwidth': 0}, # quita el borde de los tabs del notebook
                "layout": [("Notebook.tab", {"sticky": "nswe"})], # quita los tabs del notebook
            },
            "TNotebook": {
                "configure": {"borderwidth": 0}, # quita el borde de todo el notebook
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
    # crea un contenedor (notebook)
    notebook = ttk.Notebook(window)
    # configura el contenedor, para el estilo
    configure_container()
    # crea los formularios del contendor, 
    # para el escaneo de red, host y info de puertos
    tabs = create_forms(notebook)

    # inicia el menu lateral izquierdo
    side_menu.start(window, notebook, tabs)
    notebook.pack(expand=True, fill='both')
