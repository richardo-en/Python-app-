from tkinter import *
from tkinter import ttk
import frames.navigation
import frames.messages
root = Tk()
root.geometry('1000x500')
navigation_frame = frames.navigation.Navigation(root)
messages_frame = frames.messages.Messages(root)
navigation_frame.grid()
messages_frame.grid()

root.mainloop()
