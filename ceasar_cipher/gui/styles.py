from tkinter import ttk

DEFAULT_RESOLUTION = (1424, 800)
BACKGROUND_COLOR = "#0f172a"
FOREGROUND_COLOR = "#ffffff"
FONT_NAME = "Helvetica"
FONT_SIZE = 12

def setup():
    style = ttk.Style()
    style.configure(
        "TLabel",
        font=(FONT_NAME, FONT_SIZE),
        background = BACKGROUND_COLOR,
        foreground = FOREGROUND_COLOR 
    )