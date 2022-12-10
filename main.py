from static import menu
import tkinter as tk
from ttkthemes import themed_tk as tk2

window = tk2.ThemedTk()

if __name__ == "main":
    window.mainloop(menu)