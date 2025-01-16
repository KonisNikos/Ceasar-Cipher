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

        self.Toggles = [False, False, False, False]

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
        self.bruteforce_button = widgets.button(
            self.buttons_frame,
            text= "Brute Force",
            command = self.display_bruteforce_input,
            width = 12
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
        self.decode_button.pack(side = tk.LEFT, padx = 10)
        self.bruteforce_button.pack(side = tk.LEFT, padx = 10)
        self.autodecrypt_button.pack(side = tk.LEFT, padx = 10)

        self.toggle_frame = widgets.frame(self)
        self.toggle_english_button = widgets.button(
            self.toggle_frame,
            text="English",
            command=lambda: self.update_toggles(0),
            width=10
        )

        self.toggle_greek_button = widgets.button(
            self.toggle_frame,
            text="Greek",
            command=lambda: self.update_toggles(1),
            width=10
        )

        self.toggle_symbols_button = widgets.button(
            self.toggle_frame,
            text="Symbols",
            command=lambda: self.update_toggles(2),
            width=10
        )

        self.toggle_custom_button = widgets.button(
            self.toggle_frame,
            text="Custom",
            command=lambda: self.update_toggles(3),
            width=10
        )

        self.toggle_english_button.pack(side=tk.LEFT, padx=5)
        self.toggle_greek_button.pack(side=tk.LEFT, padx=5)
        self.toggle_symbols_button.pack(side=tk.LEFT, padx=5)
        self.toggle_custom_button.pack(side=tk.LEFT, padx=5)
        self.toggle_frame.pack(pady=10)

        self.custom_frame = widgets.frame(self)
        self.custom_frame.pack(pady=20, padx=20)
        self.custom_label = widgets.label(self.custom_frame, text="Custom:", padx = 5)
        self.custom_label.grid(row=0, column=0, padx=5)
        self.custom_entry = tk.Entry(self.custom_frame, width=20)
        self.custom_entry = widgets.entry(
            self.custom_frame,
            width = 30,
        )
        self.custom_entry.grid(row=0, column=1, padx=5)

        self.help_button = widgets.button(
            self,
            text="?",
            command=self.toggle_help_window,
            width=2,
            height=1,
            font=("Arial", 12, "bold"),
            bg=styles.BACKGROUND_COLOR
        )
        self.help_button.place(relx=0.97, rely=0.02, anchor=tk.NE)

        self.help_window = tk.Frame(self, width=300, height=300, bg='#3f4f76', padx=10, pady=10)
        self.help_text = tk.Label(
            self.help_window,
            text="Welcome to the Caesar Cipher app!\n\n"
                 "Use the input panel to enter text.\n"
                 "Use Encode, Decode, Brute Force or AutoDecrypt to process your text.\n"
                 "!!! Make sure to choose a key when using Encode or Decode.\n"
                 "!!! Select the toggles you want to use (English, Greek, Symbols, Custom).\n\n"
                 "Encode:\n"
                 "Cycles through the alphabet a number of places to the left. That number is the key.\n\n"
                 "Decode:\n"
                 "Cycles through the alphabet a number of places to the right. The opposite process of Encode.\n\n"
                 "Brute Force:\n"
                 "Outputs all possible decryptions with their keys.\n"
                 "Uses only the leftmost toggle.\n"
                 "Recommended to use with only one Toggle on at a time.\n\n"
                 "AutoDecrypt:\n"
                 "Outputs all possible decryptions from most likely to least.\n"
                 "!!! Only works for decryption of coherent English words. Use with English or Custom toggles.\n"
                 "Results may not be perfect if the given text is too short.\n"
                 "May also provide accurate results for non-English text, using the basic Latin alphabet though not as reliably. (French, German, Spanish etc.)\n\n"
                 "Symbols:\n"
                 "Cycles through the string:\n"
                 '''~`!1@2#3$4€%5^6&7*8(9)0_-+={[}]|:;"'<,>.?/ \n'''
                 "(there is a space in the end.)\n\n"
                 "Custom:\n"
                 "Input a string of characters to cycle through.\n"
                 "!!! Make sure all the characters are unique.\n"
                 "!!! Cannot be used with other toggles.\n\n"
                 "Click the help button (?) again to close this window.",
            justify="left",
            wraplength=600,
            bg='#3f4f76',
            fg=styles.FOREGROUND_COLOR,
            font=("Arial", 10)
        )
        self.help_text.pack()
        self.help_window.place_forget()

    def get_input(self):
        return self.input_text.get("1.0", "end-1c")


    def get_key(self):
        return self.key_entry.get()


    def get_custom(self):
        return self.custom_entry.get()


    def update_toggles(self, index):
        
        if self.Toggles[index] == True:
            self.Toggles[index] = False
        else:
            self.Toggles[index] = True
        
        if index == 3:
            for i in range(3):
                self.Toggles[i] = False
        else:
            self.Toggles[3] = False

        default_color = styles.BACKGROUND_COLOR
        active_color = styles.ACTIVE_BACKGROUND_COLOR
        Buttons = [self.toggle_english_button, self.toggle_greek_button, self.toggle_symbols_button, self.toggle_custom_button]

        for i in range(4):
            if self.Toggles[i] == True:
                Buttons[i].configure(bg=active_color)
            else:
                Buttons[i].configure(bg=default_color)


    def toggle_help_window(self):
        if self.help_window.winfo_ismapped():
            self.help_window.place_forget()
        else:
            self.help_window.place(relx=0.5, rely=0.2, anchor=tk.N)


    def display_encoded_input(self):
        key = self.get_key()
        key = int(key)
        input_text = self.get_input()
        characters = self.get_custom()
        from src.core import encode
        encoded_text=encode(input_text, key, self.Toggles, characters)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", encoded_text)
        self.output_text.config(state=tk.DISABLED)


    def display_decoded_input(self):
        key = self.get_key()
        key = int(key)
        input_text = self.get_input()
        characters = self.get_custom()
        from src.core import decode
        decoded_text=decode(input_text, key, self.Toggles, characters)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", decoded_text)
        self.output_text.config(state=tk.DISABLED)


    def display_bruteforce_input(self):
        input_text = self.get_input()
        characters = self.get_custom()
        from src.core import BruteForce
        decrypted_messages = BruteForce(input_text, self.Toggles, characters)

        self.output_text.config(state=tk.NORMAL)

        self.output_text.delete("1.0", tk.END)
        for decrypted_message in decrypted_messages:
            self.output_text.insert(tk.END, 'key = '+str(decrypted_messages[decrypted_message])+' : '+decrypted_message)
            self.output_text.insert(tk.END, "\n")

        self.output_text.config(state=tk.DISABLED)


    def display_autodecrypt_input(self):
        input_text = self.get_input()
        characters = self.get_custom()
        from src.core import AutoDecrypt
        decrypted_messages = AutoDecrypt(input_text, self.Toggles, characters)

        self.output_text.config(state=tk.NORMAL)

        self.output_text.delete("1.0", tk.END)
        for decrypted_message in decrypted_messages:
            self.output_text.insert(tk.END, 'key = '+str(decrypted_message[0])+' : '+decrypted_message[1])
            self.output_text.insert(tk.END, "\n")

        self.output_text.config(state=tk.DISABLED)