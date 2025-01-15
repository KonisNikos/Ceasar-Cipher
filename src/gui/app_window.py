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
            text="Encode", 
            command = self.display_encoded_input,
            width = 8
        ) 
        self.decode_button = widgets.button(
            self.buttons_frame,
            text = "Decode",
            command = self.display_decoded_input,
            width = 8 
        )
        self.autodecrypt_button = widgets.button(
            self.buttons_frame,
            text= "AutoDecrypt",
            command = self.display_autodecrypt_input,
            width = 12
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
        self.autodecrypt_button.pack(side = tk.LEFT, padx=10)

    def get_input(self):
        return self.input_text.get("1.0", "end-1c")


    def get_key(self):
        return self.key_entry.get()
    
    def set_Toggles(self,sentence: str):

        english_dicts = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        greek_dicts = set('αβγδεζηθικλμνξοπρστυφχψωάέήίϊΐόύϋΰώΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΆΈΉΊΪΌΎΫΏ')
        symbol_dicts = set('~`!1@2#3$4€%5^6&7*8(9)0_-+={[}]|:;"\'<,>.?/ ')
        Toggles = [False, False, False, False]

        for char in sentence:
            if char in english_dicts:
                Toggles[0] = True
            elif char in greek_dicts:
                Toggles[1] = True
            elif char in symbol_dicts:
                Toggles[2] = True
            else:
                Toggles[3] = True

        return Toggles



    def display_encoded_input(self):
        key= self.get_key()
        key=int(key)
        input_text=self.get_input()
        from src.core import encode
        Toggles=self.set_Toggles(input_text)
        encoded_text=encode(input_text,key,Toggles,"")
        self.output_text.config(state=tk.NORMAL)  
        self.output_text.delete("1.0", tk.END)  
        self.output_text.insert("1.0", encoded_text)  
        self.output_text.config(state=tk.DISABLED)
        pass


    def display_decoded_input(self):
        key= self.get_key()
        key=int(key)
        input_text=self.get_input()
        from src.core import decode
        Toggles=self.set_Toggles(input_text)
        decoded_text=decode(input_text,key,Toggles,"")
        self.output_text.config(state=tk.NORMAL)  
        self.output_text.delete("1.0", tk.END)  
        self.output_text.insert("1.0", decoded_text)  
        self.output_text.config(state=tk.DISABLED)
        pass 

    def display_autodecrypt_input(self):
        input_text=self.get_input()
        from src.core import AutoDecrypt
        Toggles=self.set_Toggles(input_text)
        decrypted_messages = AutoDecrypt(input_text, Toggles).keys()

        self.output_text.config(state=tk.NORMAL)  

        self.output_text.delete("1.0", tk.END)  
        for decrypted_message in decrypted_messages: 
            self.output_text.insert(tk.END, decrypted_message)  
            self.output_text.insert(tk.END,"\n")

        self.output_text.config(state=tk.DISABLED)