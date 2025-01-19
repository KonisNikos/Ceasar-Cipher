import tkinter as tk
from tkinter import ttk
from sys import platform

from src.gui.geometry import GeometryBuilder
from src.gui import screen
from src.gui import styles
from src.gui import widgets 
from src import core
from src.gui import config 
from src.gui import language

class AppWindow(tk.Tk):
    def __init__(self):
        #Makes text not blurry in windows devices with zoom
        if platform == "win32":
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(2)

        self.Toggles = [True, True, False, False]
        self.current_language = language.Language.ENGLISH
        self.search_history = []
        self.searchcount = 0

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

        input_label_text = language.Text(
            language.TEXTS["INPUT_LABEL"],
            self.current_language
        )
        self.input_label = widgets.label(self.input_frame, input_label_text) 

        self.output_frame = widgets.frame(self.data_frame, padx = 20, pady = 10)
        self.output_text = widgets.text(
            self.output_frame, state=tk.DISABLED,
            width = 30, height = 10,
            padx = 5, pady = 5 
        )

        output_label_text = language.Text(
            language.TEXTS["OUTPUT_LABEL"],
            self.current_language
        )
        self.output_label = widgets.label(self.output_frame, output_label_text)

        self.key_frame = widgets.frame(self)

        key_label_text = language.Text(
            language.TEXTS["KEY_LABEL"],
            self.current_language
        )
        self.key_label = widgets.label(self.key_frame, key_label_text, padx = 5)

        self.key_entry = widgets.entry(self.key_frame,width = 8)

        self.buttons_frame = widgets.frame(self)

        encode_button_text = language.Text(
            language.TEXTS["ENCODE_BUTTON"],
            self.current_language
        )
        self.encode_button = widgets.button(
            self.buttons_frame, 
            encode_button_text,
            command = self.display_encoded_input,
        )

        decode_button_text = language.Text(
            language.TEXTS["DECODE_BUTTON"],
            self.current_language
        )
        self.decode_button = widgets.button(
            self.buttons_frame,
            decode_button_text,
            command = self.display_decoded_input,
        )

        brute_force_text = language.Text(
            language.TEXTS["BRUTE_FORCE_BUTTON"],
            self.current_language
        )
        self.bruteforce_button = widgets.button(
            self.buttons_frame,
            brute_force_text,
            command = self.display_bruteforce_input,
        ) 

        auto_decrypt_text = language.Text(
            language.TEXTS["AUTO_DECRYPT_BUTTON"],
            self.current_language
        )
        self.bruteforce_button = widgets.button(
            self.buttons_frame,
            text= "Brute Force",
            command = self.display_bruteforce_input,
            width = 12
        )
        self.autodecrypt_button = widgets.button(
            self.buttons_frame,
            auto_decrypt_text,
            command = self.display_autodecrypt_input,
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

        english_toggle_text = language.Text(
            language.TEXTS["ENGLISH_TOGGLE"],
            self.current_language 
        )
        self.toggle_english_button = widgets.button(
            self.toggle_frame,
            english_toggle_text,
            command=lambda: self.update_toggles(0),
        )

        greek_toggle_text = language.Text(
            language.TEXTS["GREEK_TOGGLE"],
            self.current_language 
        )
        self.toggle_greek_button = widgets.button(
            self.toggle_frame,
            greek_toggle_text,
            command=lambda: self.update_toggles(1),
        )

        symbols_toggle_text = language.Text(
            language.TEXTS["SYMBOLS_TOGGLE"],
            self.current_language 
        )
        self.toggle_symbols_button = widgets.button(
            self.toggle_frame,
            symbols_toggle_text,
            command=lambda: self.update_toggles(2),
        )

        custom_toggle_text = language.Text(
            language.TEXTS["CUSTOM_TOGGLE"],
            self.current_language 
        )
        self.toggle_custom_button = widgets.button(
            self.toggle_frame,
            custom_toggle_text,
            command=lambda: self.update_toggles(3),
        )

        self.toggle_english_button.pack(side =tk.LEFT, padx=5)
        self.toggle_greek_button.pack(side = tk.LEFT, padx=5)
        self.toggle_symbols_button.pack(side = tk.LEFT, padx=5)
        self.toggle_custom_button.pack(side = tk.LEFT, padx=5)
        self.toggle_frame.pack(pady = 10)

        self.custom_frame = widgets.frame(self)
        self.custom_frame.pack(pady = 20, padx = 20)

        custom_label_text = language.Text(
            language.TEXTS["CUSTOM_LABEL"],
            self.current_language
        )
        self.custom_label = widgets.label(self.custom_frame, custom_label_text, padx = 5)

        self.custom_label.grid(row=0, column = 0, padx = 5)
        self.custom_entry = tk.Entry(self.custom_frame, width = 20)

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
        )
        self.help_button.place(relx=0.97, rely=0.02, anchor=tk.NE)

        self.help_window = widgets.frame(
            self, 
            bg='#111827', 
            padx=10, 
            pady=10,
            relief = tk.SOLID,
            borderwidth = 5
        )
        
        self.help_text = widgets.text(
            self.help_window,
            bg='#111827',
            fg = styles.FOREGROUND_COLOR,
            font = styles.FONT_SIZE,
            borderwidth = 0
        )
        self.help_text.insert(tk.END, config.HELP_MESSAGE)
        self.help_scrollbar = tk.Scrollbar(
            self.help_window,
            command = self.help_text.yview,
            orient = tk.VERTICAL
        )
        self.help_text.config(yscrollcommand = self.help_scrollbar.set)
        self.help_text.pack(side = tk.LEFT, padx = 10, pady = 10)
        self.help_scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

        self.help_window.place_forget()

        language_text = language.Text(
            language.TEXTS["LANGUAGE_TOGGLE"],
            self.current_language
        )
        self.switch_language_button = widgets.button(
            self,
            language_text,
            command = self.switch_language
        )
        self.switch_language_button.place(relx = 0.04, rely = 0.02)

        history_text = language.Text(
            language.TEXTS["HISTORY"], self.current_language
        )
        self.history_button = widgets.button(
            self,
            history_text,
            command=self.open_history_window,
            width=20,
        )
        self.history_button.pack(pady=15)

        self.update_toggle_colors()

    def save_history(self, mode: str, Toggles: list, input_str: str, output="N/A", key_picked="N/A"):
        self.searchcount += 1
        Toggle_str = '['
        for i in range(4):
            if Toggles[i]:
                Toggle_str += ['English, ', 'Greek, ', ' Symbols', 'Custom'][i]
        Toggle_str = Toggle_str.strip(' ').strip(',') + ']'
        self.search_history.append(f" {self.searchcount}) {mode}, Toggles: {Toggle_str}, Key: {key_picked}\nInput: {input_str}\n{output}")

    def open_history_window(self):
        history_window = tk.Toplevel(self)
        history_window.title("History")
        history_window.geometry("400x300")
        history_window.configure(bg=styles.BACKGROUND_COLOR)
        history_label = widgets.label(
            history_window, text="History:", font=("Arial", 14, "bold")
        )
        history_label.pack(pady=10)
        for item in self.search_history:
            item_label = widgets.label(history_window, text=item)
            item_label.pack(pady=2)
        close_button = widgets.button(
            history_window, text="Close", command = history_window.destroy, width=10
        )
        close_button.pack(pady=10)


    def get_input(self):
        return self.input_text.get("1.0", "end-1c")


    def get_key(self):
        return int(self.key_entry.get())


    def switch_language(self):
        if self.current_language == language.Language.ENGLISH:
            self.current_language = language.Language.GREEK
        else:
            self.current_language = language.Language.ENGLISH

        for child in self.get_children(self, [tk.Button, tk.Label]):
            child.language = self.current_language
            child.event_generate("<<onLanguageChange>>")


    @staticmethod
    def get_children(parent, filters):
        children = []
        for child in parent.winfo_children():
            for filter_type in filters:
                if isinstance(child, filter_type):
                    children.append(child)
                    break 
            children.extend(AppWindow.get_children(child, filters))
        return children


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

        self.update_toggle_colors()


    def update_toggle_colors(self):
        default_color = styles.BACKGROUND_COLOR
        active_color = styles.ACTIVE_BACKGROUND_COLOR

        buttons = [
            self.toggle_english_button, 
            self.toggle_greek_button, 
            self.toggle_symbols_button, 
            self.toggle_custom_button
        ]

        for i in range(4):
            if self.Toggles[i] == True:
                buttons[i].configure(bg = active_color)
            else:
                buttons[i].configure(bg = default_color)


    def toggle_help_window(self):
        if self.help_window.winfo_ismapped():
            self.help_window.place_forget()
        else:
            self.help_window.place(
                relx=0.5,
                rely=0.1,
                relheight = 0.7,
                relwidth = 0.75,
                anchor=tk.N
            )


    def display_encoded_input(self):
        key = self.get_key()
        input_text = self.get_input()
        characters = self.get_custom()
        encoded_text = core.encode(input_text, key, self.Toggles, characters)

        self.save_history('Encode', self.Toggles, input_text, 'Output: ' + encoded_text, key)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", encoded_text)
        self.output_text.config(state=tk.DISABLED)


    def display_decoded_input(self):
        key = self.get_key()
        input_text = self.get_input()
        characters = self.get_custom()
        decoded_text = core.decode(input_text, key, self.Toggles, characters)

        self.save_history('Decode', self.Toggles, input_text, 'Output: ' + decoded_text, key)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", decoded_text)
        self.output_text.config(state=tk.DISABLED)


    def display_bruteforce_input(self):
        input_text = self.get_input()
        characters = self.get_custom()
        decrypted_messages = core.BruteForce(input_text, self.Toggles, characters)

        self.save_history('Brute Force', self.Toggles, input_text, 'Output: (Too many results to show.)')
        self.output_text.config(state = tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        for decrypted_message in decrypted_messages:
            self.output_text.insert(
                tk.END, 
                f"key = {decrypted_messages[decrypted_message]} : {decrypted_message}"
            )
            self.output_text.insert(tk.END, "\n")
        self.output_text.config(state=tk.DISABLED)


    def display_autodecrypt_input(self):
        input_text = self.get_input()
        characters = self.get_custom()
        decrypted_messages = core.AutoDecrypt(input_text, self.Toggles, characters)

        self.save_history('AutoDecrypt', self.Toggles, input_text, 'Top result: ' + decrypted_messages[0][1])
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        for decrypted_message in decrypted_messages:
            self.output_text.insert(
                tk.END, 
                f"key = {decrypted_message[0]} : {decrypted_message[1]}"
            )
            self.output_text.insert(tk.END, "\n")
        self.output_text.config(state=tk.DISABLED)