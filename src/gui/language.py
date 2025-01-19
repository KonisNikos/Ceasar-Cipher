from enum import Enum

class Language(Enum):
    ENGLISH = 0,
    GREEK = 1

TEXTS = {
    "INPUT_LABEL": {
        Language.ENGLISH: "Input",
        Language.GREEK: "Είσοδος"
    },
    "OUTPUT_LABEL": {
        Language.ENGLISH: "Output",
        Language.GREEK: "Έξοδος"
    },
    "ENCODE_BUTTON": {
        Language.ENGLISH: "Encode",
        Language.GREEK: "Κρυπτογράφηση"
    },
    "DECODE_BUTTON": {
        Language.ENGLISH: "Decode",
        Language.GREEK: "Αποκρυπτογράφηση"
    },
    "KEY_LABEL": {
        Language.ENGLISH: "Key",
        Language.GREEK: "Κλειδί"
    },
    "BRUTE_FORCE_BUTTON": {
        Language.ENGLISH: "Brute Force",
        Language.GREEK: "Ωμή Βία"
    },
    "AUTO_DECRYPT_BUTTON": {
        Language.ENGLISH: "AutoDecrypt",
        Language.GREEK: "Αυτόματη Αποκρυπτογράφηση"
    },
    "ENGLISH_TOGGLE": {
        Language.ENGLISH: "English",
        Language.GREEK: "Αγγλικα"
    },
    "GREEK_TOGGLE": {
        Language.ENGLISH: "Greek",
        Language.GREEK: "Ελληνικά"
    },
    "SYMBOLS_TOGGLE": {
        Language.ENGLISH: "Symbols",
        Language.GREEK: "Σύμβολα"
    },
    "CUSTOM_TOGGLE": {
        Language.ENGLISH: "Custom",
        Language.GREEK: "Προσαρμοσμένο"
    },
    "CUSTOM_LABEL": {
        Language.ENGLISH: "Custom",
        Language.GREEK: "Προσαρμοσμένο"
    },
    "LANGUAGE_TOGGLE": {
        Language.ENGLISH: "English",
        Language.GREEK: "Ελληνικά"
    },
    "HISTORY": {
        Language.ENGLISH: "History",
        Language.GREEK: "Ιστορία"
    },
    "CLOSE": {
        Language.ENGLISH: "Close",
        Language.GREEK: "κλείσε"
    }
}
class Text():
    def __init__(self, texts: dict, current_language: Language | None):
        if current_language == None: 
            self.current_language = Language.ENGLISH
        self.current_language = current_language
        self.value = texts

    def get_current_text(self):
        current_text = self.value[self.current_language]
        if(current_text == None):
            return self.value.values(0)
        return self.value[self.current_language]
    
    def change_language(self, language: Language):
        self.current_language = language

    def get_language_text(self, language: Language):
        return self.value[language]