def on_select(event):
    item = event.widget.selection()[0]
    values = event.widget.item(item, 'values')
    print(values)


def restart_table(table):
    if len(table.get_children()) != 0:
        table.delete(*table.get_children())
