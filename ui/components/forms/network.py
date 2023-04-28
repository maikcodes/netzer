from scanner import network_scanner
import tkinter as tk
from tkinter import ttk

result_table = None
table_panel = None


def scan_network(network, subnet_mask):

    # scan_result = network_scanner.scan(network, subnet_mask)
    test_data = [[['192.168.1.1', '', '', 'tcp', '80', 'tcpwrapped', 'open', 'asdasd adas dasda dadasda', '', 'syn-ack', '', '8', '']], [['192.168.1.33', '', '', 'tcp', '80', 'http', 'closed', '', 'as asdasdadasda dad asd',
                                                                                                                                          'reset', '', '3', '']], [['192.168.1.36', '', '', 'tcp', '80', 'http', 'closed', '', '', 'reset', ' ada asd aasdasasd', '3', '']], [['192.168.1.38', '', '', 'tcp', '80', 'http', 'closed', '', '', 'reset', '', '3', '']]]

    refresh_table(result_table, test_data)


def refresh_table(table, data):
    global table_panel
    row_index = 1
    for host in data:
        for port in host:
            port.insert(0, f'{row_index}')
            print("...", port)
            table.insert(parent='', index='end',
                         iid=f'{host}_{port}', values=port)
            row_index += 1

    # vertical_scrollbar = ttk.Scrollbar(
    #     table, orient='vertical', command=table.yview
    # )
    # table.configure(yscrollcommand=vertical_scrollbar.set)
    # vertical_scrollbar.pack(side="right", fill="y")

    # horizontal_scrollbar = ttk.Scrollbar(
    #     table, orient='horizontal', command=table.xview
    # )
    # table.configure(xscrollcommand=horizontal_scrollbar.set)
    # horizontal_scrollbar.pack(side="bottom", fill="x")


def create_form_panel(parent):
    form_panel = tk.Frame(parent, bg='#212d40', borderwidth=50)

    # network_frame = tk.LabelFrame(form_panel, text='Network scan form', padx=20, pady=20, width=300, height=300)
    # network_frame.pack(padx=20, pady=20)
    # create the network label and entry

    network_label = tk.Label(form_panel, text="Network:",
                             background='#212d40', fg='white', font='15')
    network_label.pack(side='left', padx=2, pady=10)
    network_entry = tk.Entry(form_panel, font='18')
    network_entry.pack(side='left', padx=10, pady=10)

    subnet_label = tk.Label(form_panel, text="Subnet Mask:",
                            background='#212d40', fg='white', font='15')
    subnet_label.pack(side='left', padx=2, pady=10)
    subnet_entry = tk.Entry(form_panel, font='18')
    subnet_entry.pack(side='left', padx=10, pady=10)

    scan_button = tk.Button(
        form_panel, text="SCAN",
        command=lambda: scan_network(
            network_entry.get(),
            subnet_entry.get()
        ), background='#4dff88', font='20')
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
    # table_panel = tk.Frame(parent, bg='red', background='#212d40')
    table_panel = tk.Frame(parent, bg='#212d40')
    table = ttk.Treeview(table_panel, padding='5', height='200')

    # define the columns
    table['columns'] = ('#', 'host', 'hostname', 'hostname_type', 'protocol', 'port', 'name',
                        'state', 'product', 'extrainfo', 'reason', 'version', 'conf', 'cpe')

    table.heading('#', text='n', anchor=tk.CENTER)
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

    table.column('#', anchor=tk.CENTER)
    table.column('host', anchor=tk.CENTER)
    table.column('hostname', anchor=tk.CENTER)
    table.column('hostname_type', anchor=tk.CENTER)
    table.column('protocol', anchor=tk.CENTER)
    table.column('port', anchor=tk.CENTER)
    table.column('name', anchor=tk.CENTER)
    table.column('state', anchor=tk.CENTER)
    table.column('product', anchor=tk.CENTER)
    table.column('extrainfo', anchor=tk.CENTER)
    table.column('reason', anchor=tk.CENTER)
    table.column('version', anchor=tk.CENTER)
    table.column('conf', anchor=tk.CENTER)
    table.column('cpe', anchor=tk.CENTER)

    table.bind('<<TreeviewSelect>>', on_select)

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
