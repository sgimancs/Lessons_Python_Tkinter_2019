#############################################
# SAMPLE (TTK)
# Bottom TTK style
#############################################

from tkinter import ttk
from tkinter import Tk

root = Tk()
style = ttk.Style()

button_1 = ttk.Button(root, text='click me')

style.theme_use('alt')
style.configure('TButton', font=('Helvetica', 14), background='blue', foreground='white')
style.map('TButton', background=[('active', 'green')])
button_1.pack()

root.mainloop()
