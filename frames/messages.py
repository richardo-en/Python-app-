import tkinter as tk


class Messages(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.configure(background='#fff')
        self.grid(row=0, column=1,  sticky='news')

        master.columnconfigure(1, weight=1)

        self.label = tk.Label(
            self, text="Messsssages", background='#fff', fg='black', font=('Helvetica bold', 14))
        self.label.grid(row=0, column=0, sticky='nsew', pady=10)

        self.grid_columnconfigure(0, weight=1)
