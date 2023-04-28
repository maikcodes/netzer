import tkinter as tk
from tkinter import ttk, scrolledtext

# Create the main window
root = tk.Tk()

# Create a Treeview with one column
treeview = ttk.Treeview(root)
treeview.pack()

# Add a column to the Treeview
treeview['columns'] = ('description',)

# Define the column
treeview.column('#0', width=150)
treeview.column('description', width=200, stretch=tk.YES)

# Define the column headings
treeview.heading('#0', text='Name')
treeview.heading('description', text='Description')

# Add some sample data
item1 = treeview.insert('', 'end', text='Item 1')
item2 = treeview.insert('', 'end', text='Item 2')
frame1 = tk.Frame(treeview, relief='sunken', bd=1)
text1 = scrolledtext.ScrolledText(frame1, wrap=tk.WORD, width=30, height=4)
text1.pack()
treeview.insert(item1, 'end', values=('Description for item 1', frame1))
treeview.insert(item2, 'end', values=('Description for item 2', 'Second column'))

# Start the main loop
root.mainloop()
