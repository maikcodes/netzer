def on_select(event):
    item = event.widget.selection()[0]
    values = event.widget.item(item, 'values')
    print(values)
