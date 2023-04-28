import json
import tkinter as tk
from tkinter import ttk

result_table = None
table_panel = None


def create_ports_list_table(parent):
    table_panel = tk.Frame(parent, bg='#212d40')
    table = ttk.Treeview(table_panel, padding='5', height='200')

    table['columns'] = ('#', 'port', 'protocol', 'name', 'description')

    anchor = tk.NW

    table.column('#', width=50, anchor='center', stretch=False)
    table.column('port', width=30, anchor='w')
    table.column('protocol', anchor=anchor, width='30')
    table.column('name', width=30, anchor="w", stretch=False)
    table.column('description', width=30, anchor="w", stretch=False)

    table.heading('#', text='#')
    table.heading('port', text='Port')
    table.heading('protocol', text='Protocol')
    table.heading('name', text='Name')
    table.heading('description', text='Description')

    vertical_scrollbar = ttk.Scrollbar(
        table_panel, orient='vertical', command=table.yview
    )
    table.configure(yscrollcommand=vertical_scrollbar.set)
    vertical_scrollbar.pack(side="right", fill="y")

    horizontal_scrollbar = ttk.Scrollbar(
        table_panel, orient='horizontal', command=table.xview
    )
    table.configure(xscrollcommand=horizontal_scrollbar.set)
    horizontal_scrollbar.pack(side="bottom", fill="x")
    table.pack(padx=30, pady=40)

    with open('ui/components/forms/ports.json') as f:
        data = json.load(f)

    result = []

    row_index = 1
    for key, value in data.items():
        parts = key.split("/")
        port_number = parts[0]
        protocol = parts[1]
        name = value["name"]
        description = value.get("description", "")

        result.append([row_index, port_number, protocol, name, description])
        row_index += 1

    for port in result:
        table.insert(parent='', index='end', iid=f'{port}', values=port)

    global result_table
    result_table = table
    result_table.pack(fill='both')
    return table_panel


def create(tab):
    print('table', result_table)
    table_panel = create_ports_list_table(tab)
    print('table', result_table)
    table_panel.pack(side='bottom', fill='both', expand=True)
