from .middleware import on_select, restart_table
from scanner import network_scanner
import tkinter as tk
from tkinter import Entry, Button, Frame, Label, Scrollbar
from tkinter.ttk import Treeview


result_table = None
table_panel = None


def scan_network(network, subnet_mask, ports):
    scan_result = network_scanner.scan(network, subnet_mask, ports)
    refresh_table(result_table, scan_result)


def refresh_table(table, data):
    restart_table(table)

    global table_panel
    row_index = 1

    for host in data:
        for port in host:
            port.insert(0, row_index)
            table.insert(
                parent='', index='end', iid=f'{host}_{port}', values=port
            )
            row_index += 1


def create_form_panel(parent):

    form_panel = Frame(parent, bg='#212d40', borderwidth=50)

    network_label = Label(
        form_panel, text='Network:', background='#212d40', fg='white', font='15'
    )
    network_label.pack(side='left', padx=2, pady=10)
    network_entry = Entry(form_panel, font='18')
    network_entry.pack(side='left', padx=10, pady=10)

    subnet_label = Label(
        form_panel, text='Subnet Mask:', background='#212d40', fg='white', font='15'
    )
    subnet_label.pack(side='left', padx=2, pady=10)
    subnet_entry = Entry(form_panel, font='18')
    subnet_entry.pack(side='left', padx=10, pady=10)

    ports_label = Label(
        form_panel, text='Ports:', background='#212d40', fg='white', font='15'
    )
    ports_label.pack(side='left', padx=2, pady=10)
    ports_entry = Entry(form_panel, font='18')
    ports_entry.pack(side='left', padx=10, pady=10)

    scan_button = Button(
        form_panel, text='SCAN',
        command=lambda: scan_network(network_entry.get(), subnet_entry.get(), ports_entry.get()), background='#4dff88', font='20'
    )
    scan_button.pack(side='left')

    return form_panel


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
    horizontal_scrollbar.pack(side='bottom', fill='x', padx='10')


def table_structure(table):
    table['columns'] = (
        'index', 'host', 'hostname', 'hostname_type', 'protocol', 'port', 'name',
        'state', 'product', 'extrainfo', 'reason', 'version', 'conf', 'cpe'
    )

    table.heading('#0', text='', anchor='center')
    table.heading('index', text='N', anchor='center')
    table.heading('host', text='Host', anchor='center')
    table.heading('hostname', text='Hostname', anchor='center')
    table.heading('hostname_type', text='Hostname type', anchor='center')
    table.heading('protocol', text='Protocol', anchor='center')
    table.heading('port', text='Port', anchor='center')
    table.heading('name', text='Name', anchor='center')
    table.heading('state', text='State', anchor='center')
    table.heading('product', text='Product', anchor='center')
    table.heading('extrainfo', text='Extrainfo', anchor='center')
    table.heading('reason', text='Reason', anchor='center')
    table.heading('version', text='Version', anchor='center')
    table.heading('conf', text='Conf', anchor='center')
    table.heading('cpe', text='CPE', anchor='center')

    table.column('#0', width='0', stretch=tk.NO)
    table.column('index', anchor='center', width='30')
    table.column('host', anchor='center', width='100')
    table.column('hostname', anchor='center')
    table.column('hostname_type', anchor='center')
    table.column('protocol', anchor='center', width='60')
    table.column('port', anchor='center', width='30')
    table.column('name', anchor='center')
    table.column('state', anchor='center', width='50')
    table.column('product', anchor='center', stretch=tk.YES, width='200')
    table.column('extrainfo', anchor='center')
    table.column('reason', anchor='center')
    table.column('version', anchor='center')
    table.column('conf', anchor='center')
    table.column('cpe', anchor='center')
    table.columnconfigure(6, minsize=200)


def create_table(panel):
    table = Treeview(panel, height='200')
    configure_table(table=table, panel=panel)
    return table


def create_table_panel(parent):
    table_panel = Frame(parent, bg='#212d40')
    table = create_table(panel=table_panel)
    global result_table
    result_table = table
    result_table.pack()
    return table_panel


def start(tab):
    form_panel = create_form_panel(tab)
    table_panel = create_table_panel(tab)
    form_panel.pack(side='top', fill='x')
    table_panel.pack(side='bottom', fill='both', expand=True)
