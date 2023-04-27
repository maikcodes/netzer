from scanner import network_scanner
import tkinter as tk
from tkinter import ttk

result_table = None


def scan_network():
    scan_result = network_scanner.scan()

    refresh_table(result_table, scan_result)


def refresh_table(table, data):
    for host in data:
        for port in host:
            table.insert(parent='', index='end',
                         iid=f'{host}_{port}', values=port)


def create_form_panel(parent):
    form_panel = tk.Frame(parent, bg='blue', width=800, height=400)

    # create the network label and entry
    network_label = tk.Label(form_panel, text="Network:")
    network_label.pack()
    network_entry = tk.Entry(form_panel)
    network_entry.pack()

    # create the subnet mask label and entry
    subnet_label = tk.Label(form_panel, text="Subnet Mask:")
    subnet_label.pack()
    subnet_entry = tk.Entry(form_panel)
    subnet_entry.pack()

    # create the scan button
    scan_button = tk.Button(form_panel, text="Run Scan",
                            command=lambda: scan_network())
    scan_button.pack()

    return form_panel


def create_table_panel(parent):
    table_panel = tk.Frame(parent, bg='red', width=800, height=100)
    table = ttk.Treeview(table_panel)

    # define the columns
    table['columns'] = ('host', 'hostname', 'hostname_type', 'protocol', 'port', 'name',
                        'state', 'product', 'extrainfo', 'reason', 'version', 'conf', 'cpe')

    table.column('#0', width=0, stretch=tk.NO)
    table.column('host', anchor=tk.CENTER, width=80)
    table.column('hostname', anchor=tk.CENTER, width=80)
    table.column('hostname_type', anchor=tk.CENTER, width=80)
    table.column('protocol', anchor=tk.CENTER, width=80)
    table.column('port', anchor=tk.CENTER, width=80)
    table.column('name', anchor=tk.CENTER, width=80)
    table.column('state', anchor=tk.CENTER, width=80)
    table.column('product', anchor=tk.CENTER, width=80)
    table.column('extrainfo', anchor=tk.CENTER, width=80)
    table.column('reason', anchor=tk.CENTER, width=80)
    table.column('version', anchor=tk.CENTER, width=80)
    table.column('conf', anchor=tk.CENTER, width=80)
    table.column('cpe', anchor=tk.CENTER, width=80)

    table.column('#0', width=0, stretch=tk.NO)
    table.heading('host', text='host', anchor=tk.CENTER)
    table.heading('hostname', text='hostname', anchor=tk.CENTER)
    table.heading('hostname_type', text='hostname_type', anchor=tk.CENTER)
    table.heading('protocol', text='protocol', anchor=tk.CENTER)
    table.heading('port', text='port', anchor=tk.CENTER)
    table.heading('name', text='name', anchor=tk.CENTER)
    table.heading('state', text='state', anchor=tk.CENTER)
    table.heading('product', text='product', anchor=tk.CENTER)
    table.heading('extrainfo', text='extrainfo', anchor=tk.CENTER)
    table.heading('reason', text='reason', anchor=tk.CENTER)
    table.heading('version', text='version', anchor=tk.CENTER)
    table.heading('conf', text='conf', anchor=tk.CENTER)
    table.heading('cpe', text='cpe', anchor=tk.CENTER)

    global result_table
    result_table = table
    result_table.pack()
    return table_panel


def create(tab):
    print('table', result_table)
    form_panel = create_form_panel(tab)
    table_panel = create_table_panel(tab)
    print('table', result_table)
    form_panel.pack(side='top', fill='x')
    table_panel.pack(side='bottom', fill='both', expand=True)
