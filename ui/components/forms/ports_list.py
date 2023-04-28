import json
from .middleware import on_select
import tkinter as tk
from tkinter import Frame, Scrollbar
from tkinter.ttk import Treeview


def configure_table(table, panel):
    table_structure(table)
    table_on_select(table)
    table_scrollbar_XY(table, panel)
    table.pack(padx='10', pady='10')


def table_on_select(table):
    table.bind('<<TreeviewSelect>>', on_select)


def table_scrollbar_XY(table, panel):
    vertical_scrollbar = Scrollbar(
        panel, orient='vertical', command=table.yview
    )
    table.configure(yscrollcommand=vertical_scrollbar.set)
    vertical_scrollbar.pack(side='right', fill='y')

    horizontal_scrollbar = Scrollbar(
        panel, orient='horizontal', command=table.xview
    )
    table.configure(xscrollcommand=horizontal_scrollbar.set)


def table_structure(table):
    table['columns'] = ('#', 'port', 'protocol', 'name', 'description')

    table.column('#0', width='0', stretch=tk.NO)
    table.column('#', anchor='center', width='10')
    table.column('port', anchor='center', width='10')
    table.column('protocol', anchor='center', width='20')
    table.column('name', anchor='center')
    table.column('description', anchor='center')

    table.heading('#0', text='', anchor='center')
    table.heading('#', text='#')
    table.heading('port', text='Port')
    table.heading('protocol', text='Protocol')
    table.heading('name', text='Name')
    table.heading('description', text='Description')


def create_table(panel):
    table = Treeview(panel, height='200')
    configure_table(table=table, panel=panel)
    return table


def create_ports_list_table(parent):
    table_panel = Frame(parent, bg='#212d40')
    table = create_table(panel=table_panel)

    with open('ui/components/forms/ports.json') as f:
        data = json.load(f)

    result = []

    row_index = 1
    for key, value in data.items():
        parts = key.split('/')
        port_number = parts[0]
        protocol = parts[1]
        name = value['name']
        description = value.get('description', '')

        result.append([row_index, port_number, protocol, name, description])
        row_index += 1

    for port in result:
        table.insert(parent='', index='end', iid=f'{port}', values=port)

    table.pack(fill='both')
    return table_panel


def create(tab):
    table_panel = create_ports_list_table(tab)
    table_panel.pack(side='bottom', fill='both', expand=True)
