import tkinter as tk
from src.gui import styles 
from src.gui import geometry

def frame(parent, **kargs):
    kargs.setdefault("bg", styles.BACKGROUND_COLOR)
    return tk.Frame(parent, **kargs)

@styles.apply_text_styles
def label(parent, **kargs):
    return tk.Label(parent, **kargs)

@styles.apply_text_styles
def text(parent, **kargs):
    kargs.setdefault("insertbackground", styles.FOREGROUND_COLOR)
    return tk.Text(parent, **kargs)

@styles.apply_text_styles
def entry(parent, **kargs):
    kargs.setdefault("insertbackground", styles.FOREGROUND_COLOR)
    return tk.Entry(parent, **kargs)

@styles.apply_text_styles
def button(parent, **kargs):
    kargs.setdefault("activebackground", styles.ACTIVE_BACKGROUND_COLOR)
    kargs.setdefault("activeforeground", styles.FOREGROUND_COLOR)
    return tk.Button(parent, **kargs)

