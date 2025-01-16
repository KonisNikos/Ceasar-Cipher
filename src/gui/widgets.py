import tkinter as tk
from src.gui import styles 
from src.gui import geometry

def frame(parent, **kargs):
    kargs.setdefault("bg", styles.BACKGROUND_COLOR)
    return tk.Frame(parent, **kargs)

@styles.apply_text_styles
def label(parent, text, **kargs):  
    if isinstance(text, str):
        kargs.setdefault("text", text)
        return tk.Label(parent, **kargs)

    text_value = text.get_current_text()  
    kargs.setdefault("text", text_value)
    label = tk.Label(parent, **kargs)

    def on_language_change(event):
        language = event.widget.language
        current_text = text.get_language_text(language)
        label.configure(text = current_text) 
    label.bind("<<onLanguageChange>>", on_language_change)
    return label

@styles.apply_text_styles
def text(parent, **kargs):
    kargs.setdefault("insertbackground", styles.FOREGROUND_COLOR)
    return tk.Text(parent, **kargs)

@styles.apply_text_styles
def entry(parent, **kargs):
    kargs.setdefault("insertbackground", styles.FOREGROUND_COLOR)
    return tk.Entry(parent, **kargs)

@styles.apply_text_styles
def button(parent, text, **kargs):
    kargs.setdefault("activebackground", styles.ACTIVE_BACKGROUND_COLOR)
    kargs.setdefault("activeforeground", styles.FOREGROUND_COLOR)

    if isinstance(text, str):
        kargs.setdefault("text", text)
        return tk.Button(parent, **kargs)

    text_value = text.get_current_text()  
    kargs.setdefault("text", text_value)
    button = tk.Button(parent, **kargs)

    def on_language_change(event):
        language = event.widget.language
        current_text = text.get_language_text(language)
        button.configure(text = current_text) 
    button.bind("<<onLanguageChange>>", on_language_change)

    return button 

