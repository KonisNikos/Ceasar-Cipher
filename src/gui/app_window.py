import tkinter as tk
from tkinter import ttk
from sys import platform

from src.gui.geometry import GeometryBuilder
from src.gui import screen
from src.gui import styles
from src.gui import widgets 

class AppWindow(tk.Tk):
    def __init__(self):
        #Makes text not blurry in windows devices with zoom
        if platform == "win32":
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(2)

        super().__init__()

        self.title("Ceasar Cipher")

        screen_dimentions = screen.get_screen_dimentions(self)
        geometry_string = GeometryBuilder(screen_dimentions).center().build()
        self.geometry(geometry_string)

        self.configure(bg = styles.BACKGROUND_COLOR)
        self.data_frame = widgets.frame(self) 

        self.input_frame = widgets.frame(self.data_frame, padx = 20, pady = 10)        
        self.input_text = widgets.text(
            self.input_frame, 
            width = 30, height = 10,
            padx = 5, pady = 5, 
        )
        self.input_label = widgets.label(self.input_frame, text="Input:")

        self.output_frame = widgets.frame(self.data_frame, padx = 20, pady = 10)
        self.output_text = widgets.text(
            self.output_frame, state=tk.DISABLED,
            width = 30, height = 10,
            padx = 5, pady = 5 
        )
        self.output_label = widgets.label(self.output_frame, text="Output:")

        self.key_frame = widgets.frame(self)
        self.key_label = widgets.label(self.key_frame, text="key:", padx = 5)
        self.key_entry = widgets.entry(
            self.key_frame,
            width = 8,
        ) 
        self.buttons_frame = widgets.frame(self)
        self.encode_button = widgets.button(
            self.buttons_frame, 
            text="encode", 
            command = self.display_encoded_input,
            width = 8
        ) 
        self.decode_button = widgets.button(
            self.buttons_frame,
            text = "decode",
            command = self.display_decoded_input,
            width = 8 
        )

        self.input_frame.pack(side = tk.LEFT)
        self.output_frame.pack(side = tk.RIGHT)

        self.input_label.pack(side=tk.TOP, pady=5)
        self.input_text.pack(side = tk.BOTTOM)

        self.output_label.pack(side = tk.TOP, pady = 5)
        self.output_text.pack(side = tk.BOTTOM)
        

        self.data_frame.pack()

        self.key_frame.pack(pady = 10)
        self.key_label.pack(side = tk.LEFT)
        self.key_entry.pack(side = tk.RIGHT)

        self.buttons_frame.pack(pady = 15)
        self.encode_button.pack(side = tk.LEFT, padx = 10)
        self.decode_button.pack(side = tk.RIGHT, padx = 10)

    def get_input(self):
        return self.input_text.get("1.0", "end-1c")


    def get_key(self):
        return self.key_entry.get("1.0", "end-1c")


    def display_encoded_input(self):
        '''
        task:

        When this function is called it has to update the self.output_text
        Its contents should contain the encoded input data 
        Hint 1: Call self.get_input and self.get_key to get the input and key
        data 
        Hint 2: IMPORTANT! You first need to configure the state of the
        output_text to normal so you can write info to it
        Hint 3: read https://tkdocs.com/tutorial/text.html to figure how 
        indexing works.
        Hint 4: the encode function is at the core file 
        ''' 
        pass


    def display_decoded_input(self):
        '''
        Similar concept with the encode funcition maybe 
        create another function to help clear things up
        '''
        pass 