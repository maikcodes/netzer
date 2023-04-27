from scanner import network_scanner
import tkinter as tk
from tkinter import ttk

result_table = None


def scan_network(network, subnet_mask):

    scan_result = network_scanner.scan(network, subnet_mask)
    # test_data = [[['192.168.1.1', '', '', 'tcp', '80', 'tcpwrapped', 'open', '', '', 'syn-ack', '', '8', '']], [['192.168.1.33', '', '', 'tcp', '80', 'http', 'closed', '', '', 'reset', '', '3', '']], [['192.168.1.36', '', '', 'tcp', '80', 'http', 'closed', '', '', 'reset', '', '3', '']], [['192.168.1.38', '', '', 'tcp', '80', 'http', 'closed', '', '', 'reset', '', '3', '']]]

    refresh_table(result_table, scan_result)


def refresh_table(table, data):
    for host in data:
        for port in host:
            table.insert(parent='', index='end',
                         iid=f'{host}_{port}', values=port)


def create_form_panel(parent):
    form_panel = tk.Frame(parent, bg='blue', width=800, height=400, borderwidth=50, background='#212d40')

    # network_frame = tk.LabelFrame(form_panel, text='Network scan form', padx=20, pady=20, width=300, height=300)
    # network_frame.pack(padx=20, pady=20)
    # create the network label and entry

    network_label = tk.Label(form_panel, text="Network:", background='#212d40', fg='white')
    network_label.pack(side='left', padx=2, pady=10)
    network_entry = tk.Entry(form_panel)
    network_entry.pack(side='left', padx=10, pady=10)

    subnet_label = tk.Label(form_panel, text="Subnet Mask:", background='#212d40', fg='white')
    subnet_label.pack(side='left', padx=2, pady=10)
    subnet_entry = tk.Entry(form_panel)
    subnet_entry.pack(side='left', padx=10, pady=10)

    scan_button = tk.Button(
        form_panel, text="Run Scan",
        command=lambda: scan_network(
            network_entry.get(),
            subnet_entry.get()
        )
    , background='#4dff88')
    scan_button.pack(side='left')

    return form_panel


def on_select(event):
    # get the selected item
    item = event.widget.selection()[0]
    # get the values of the selected item
    values = event.widget.item(item, 'values')
    # print the values of the selected item
    print(values)


def create_table_panel(parent):
    table_panel = tk.Frame(parent, bg='red', width=800, height=100, background='#212d40')
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

    table.bind('<<TreeviewSelect>>', on_select)
    table.pack(fill='both', padx=10, pady=10)

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
