import tkinter as tk


class Navigation(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.configure(background='#343A40')
        self.grid(row=0, column=0,  sticky='news')
        names = ["Messages", "Settings", "Console"]
        name_number = 0
        configuration = [{'background': '#343A40'}, {'fg': 'white'}, {'borderwidth': 0}, {
            'height': 2}, {'activeforeground': '#fff'}, {'activebackground': '#495057'}]

        master.columnconfigure(0, minsize=200)
        master.rowconfigure(0, weight=1)

        self.label = tk.Label(self, text="NoNameApp")
        self.label.config(font=('Helvetica bold', 12))
        self.label.grid(row=0, column=0, sticky='nsew', pady=10)

        for i in range(1, 4):
            self.button = tk.Button(self)
            self.button.grid(row=i, column=0, sticky='ew')

        for widget in self.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(configuration, text=names[name_number], font=(
                    'Helvetica bold', 12))
                name_number += 1
        self.grid_columnconfigure(0, weight=1)
