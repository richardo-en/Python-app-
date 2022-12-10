from tkinter import ttk
from ttkthemes import ThemedTk
from models.functions import choose_file

window = ThemedTk()
window.get_themes()
window.set_theme("equilux")
window.geometry("400x200")


button = ttk.Button(window, text="Choose file", command=choose_file)
button.pack()


ttk.Button(window, text="Quit", command=window.destroy).pack()
window.mainloop()
