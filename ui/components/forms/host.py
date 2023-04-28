from .middleware import on_select
from scanner import host_scanner
import tkinter as tk
from tkinter import ttk, Entry, Button, Frame, Label, Scrollbar

result_table = None
table_panel = None


def scan_hosts(network, ports):
    scan_result = host_scanner.scan(network, ports)
    refresh_table(result_table, scan_result)


def refresh_table(table, data):
    global table_panel
    row_index = 1

    for port in data:
        port.insert(0, row_index)
        table.insert(
            parent='', index='end', iid=f'{port}', values=port
        )
        row_index += 1


def create_form_panel(parent):

    form_panel = Frame(parent, bg='#212d40', borderwidth=50)

    network_label = Label(
        form_panel, text="Network:", background='#212d40', fg='white', font='15'
    )
    network_label.pack(side='left', padx=2, pady=10)
    network_entry = Entry(form_panel, font='18')
    network_entry.pack(side='left', padx=10, pady=10)

    ports_label = Label(
        form_panel, text="Ports:", background='#212d40', fg='white', font='15'
    )
    ports_label.pack(side='left', padx=2, pady=10)
    ports_entry = Entry(form_panel, font='18')
    ports_entry.pack(side='left', padx=10, pady=10)

    scan_button = Button(
        form_panel, text="SCAN",
        command=lambda: scan_hosts(network_entry.get(), ports_entry.get()), background='#4dff88', font='20'
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
    vertical_scrollbar.pack(side="right", fill="y")

    horizontal_scrollbar = Scrollbar(
        panel, orient='horizontal', command=table.xview
    )
    table.configure(xscrollcommand=horizontal_scrollbar.set)
    horizontal_scrollbar.pack(side="bottom", fill="x", padx='10')


def table_structure(table):
    table['columns'] = (
        'index', 'host', 'hostname', 'hostname_type', 'protocol', 'port', 'name',
        'state', 'product', 'extrainfo', 'reason', 'version', 'conf', 'cpe'
    )

    table.heading('#0', text='', anchor=tk.CENTER)
    table.heading('index', text='N', anchor=tk.CENTER)
    table.heading('host', text='Host', anchor=tk.CENTER)
    table.heading('hostname', text='Hostname', anchor=tk.CENTER)
    table.heading('hostname_type', text='Hostname type', anchor=tk.CENTER)
    table.heading('protocol', text='Protocol', anchor=tk.CENTER)
    table.heading('port', text='Port', anchor=tk.CENTER)
    table.heading('name', text='Name', anchor=tk.CENTER)
    table.heading('state', text='State', anchor=tk.CENTER)
    table.heading('product', text='Product', anchor=tk.CENTER)
    table.heading('extrainfo', text='Extrainfo', anchor=tk.CENTER)
    table.heading('reason', text='Reason', anchor=tk.CENTER)
    table.heading('version', text='Version', anchor=tk.CENTER)
    table.heading('conf', text='Conf', anchor=tk.CENTER)
    table.heading('cpe', text='CPE', anchor=tk.CENTER)

    table.column('#0', width='0', stretch=tk.NO)
    table.column('index', anchor=tk.CENTER, width='30')
    table.column('host', anchor=tk.CENTER, width='100')
    table.column('hostname', anchor=tk.CENTER)
    table.column('hostname_type', anchor=tk.CENTER)
    table.column('protocol', anchor=tk.CENTER, width='60')
    table.column('port', anchor=tk.CENTER, width='30')
    table.column('name', anchor=tk.CENTER)
    table.column('state', anchor=tk.CENTER, width='50')
    table.column('product', anchor=tk.CENTER, stretch=tk.YES, width='200')
    table.column('extrainfo', anchor=tk.CENTER)
    table.column('reason', anchor=tk.CENTER)
    table.column('version', anchor=tk.CENTER)
    table.column('conf', anchor=tk.CENTER)
    table.column('cpe', anchor=tk.CENTER)
    table.columnconfigure(6, minsize=200)


def create_table(panel):
    table = ttk.Treeview(panel, height='200')
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
