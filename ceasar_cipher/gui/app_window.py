import tkinter as tk
from tkinter import ttk
from sys import platform
from gui.geometry import GeometryBuilder
from gui import styles

class AppWindow(tk.Tk):
    def __init__(self):
        #Makes text not blurry in windows devices with zoom
        if platform == "win32":
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(2)

        super().__init__()
        styles.setup()
        self.title("Hello World")
        geometry_string = GeometryBuilder(self).center().build()
        self.geometry(geometry_string)

        self.configure(bg = styles.BACKGROUND_COLOR)
        self.label = ttk.Label(
            self, text="Hello World", style="TLabel"
        )
        self.label.pack()
