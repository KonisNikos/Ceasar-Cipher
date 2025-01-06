from enum import Enum
from sys import intern


class Language(Enum):
    ENGLISH = 1      
    GREEK = 2
    SYMBOLS = 3

CHARACTER_SETS = {
    Language.ENGLISH: [
        intern("abcdefghijklmnopqrstuvwxyz"),
        intern("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    ],
    Language.GREEK: [
        intern("αβγδεζηθικλμνξοπρστυφχψω"),
        intern("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ")
    ],
# TODO: Add a preview of the syms string below to show which and how the characters will rotate.
    Language.SYMBOLS: [
        intern('''~`!1@2#3$4€%5^6&7*8(9)0_-+={[}]|:;"'<,>.?/''')
    ]
}
class CharacterSetBuilder():
    def __init__(self): 
        self.custom = False
        self.character_sets = []
        self.used_languages = []


    def from_list(self, languages: list[Language]):
        if not isinstance(languages, list[Language]): 
            languages_type = type(languages).__name__
            raise TypeError(f"Expected a Languages list, got {languages_type}")

        for language in languages:
            self.add(language)

        return self


    def add(self, language: Language):
        if not isinstance(language, Language):
            return TypeError(f"Expected a Language type, got {toggles_list_type}")
        if language in self.used_languages:
            raise Exception(f"Can't add the same language a second time")

        self.character_sets += CHARACTER_SETS[language]
        self.used_languages += [language]
        return self


    def add_all(self):
        character_sets = []
        for language in Language:
            self.add(language)
        return self


    def add_custom(self, custom_text):
        self.custom = True
        self.character_sets[0] = custom_text
        return self
    

    def build(self):
        if(self.custom and len(self.used_languages) > 0):
            raise Exception("You can not add a custom alphabet and the normal one")
        if(len(self.character_sets) == 0):
            raise Exception("You need to add at least one character set")
        return self.character_sets

# TODO: Add toggles to the UI for the options: English, Greek, Symbols and Numbers, Custom.
def encode(plain_text: str, key: int, character_sets: list[str]):
    if not isinstance(plain_text, str):
        raise TypeError(f"Expected a str, got {type(plain_text).__name__}")
    if not isinstance(key, int):
        raise TypeError(f"Expected an int, got {type(key).__name__}")

    if len(character_sets) == 0:
        raise Exception("No character sets were provided")

    cipher_text = ""
    for character in plain_text:
        encrypted_character = character
        for character_set in character_sets:
            if(character not in character_set):
                continue
            character_index = character_set.index(character)
            set_length = len(character_set)
            encrypted_character = character_set[(character_index - key) % set_length]
            break
        cipher_text += encrypted_character

    return cipher_text


def decode(cipher_text: str, key: int, character_sets):
    return encode(cipher_text, -key, character_sets)


def BruteForce(cipher_text: str, character_sets: list[str]):
    if not isinstance(cipher_text, str):
        raise TypeError(f"Expected a str, got {type(cipher_text).__name__}")
    character_set_length = len(character_sets[0])

    result = {}
    for key in range(character_set_length):
        result.setdefault(decode(cipher_text, key, character_sets), key)

    return result 


# The following N-grams are the most common, taken from their respective wikipedia page (if it exists)
# and/or from the site: https://www3.nd.edu/~busiforc/handouts/cryptography/Letter%20Frequencies.html
Bigrams = {'th':2, 'he':2, 'in':2, 'er':2, 'an':2, 're':2, 'on':2, 'at':2, 'en':2, 'nd':2, 'ti':2, 'es':2, 'or':2, 'te':2, 'of':2, 'ed':2, 'is':2, 'it':2, 'al':2, 'ar':2, 'st':2,
           'to':1, 'nt':1, 'ng':1, 'se':1, 'ha':1, 'as':1, 'ou':1, 'io':1, 'le':1, 've':1, 'co':1, 'me':1, 'de':1, 'hi':1, 'ri':1, 'ro':1, 'ic':1, 'ne':1, 'ea':1, 'ra':1, 'ce':1}

Trigrams = {'the':5, 'and':5, 'ing':5, 'her':5, 'hat':5, 'his':5, 'tha':5, 'ere':5, 'for':5, 'ent':5, 'ion':5, 'ter':5, 'was':5, 'you':5,
            'ith':4, 'ver':4, 'all':4, 'wit':4, 'thi':4, 'tio':4, 'nde':4, 'has':4, 'nce':4, 'edt':4, 'tis':4, 'oft':4, 'sth':4, 'men':4}

Quadrigrams = {'that':6, 'ther':6, 'with':6, 'tion':6, 'here':6, 'ould':6, 'ight':6, 'have':6, 'hich':6, 'whic':6,
               'this':6, 'thin':6, 'they':6, 'atio':6, 'ever':6, 'from':6, 'ough':6, 'were':6, 'hing':6, 'ment':6}


# Altered so it can be used to sort a dictionary and do so in reverse order.
def QuickSort(Dict: dict, List: list):
    if len(List) < 2: return List
    i = 0
    for j in range(len(List)-1):
        if Dict[List[j]] > Dict[List[-1]]:
            List[i], List[j] = List[j], List[i]
            i += 1
    List[i], List[-1] = List[-1], List[i]

    Left = QuickSort(Dict, List[:i])
    Right = QuickSort(Dict, List[i+1:])

    return Left + [List[i]] + Right


# TODO: Add a disclaimer when choosing this function stating the below.
# Only works for decryption of coherent English words! Use with English or Custom ciphers.
# Results may not be perfect if the text is too short.
def AutoDecrypt(cipher_text: str):

    if not isinstance(cipher_text, str):
        raise TypeError(f"Expected a str, got {type(cipher_text).__name__}")

    english_set = CharacterSetBuilder().add(Language.ENGLISH).build()
    PossibleDecryptions = BruteForce(cipher_text, english_set) 
    DecryptionScores = {}

    for decrypted_message in PossibleDecryptions:
        key = PossibleDecryptions[decrypted_message]
        points = 0

        modified_message = decrypted_message.lower()

        for i in range(1, 4):
            Ngrams = [Bigrams, Trigrams, Quadrigrams][i-1]
            for j in range(len(modified_message)-i):
                if modified_message[j: j+i+1] in Ngrams:
                    points += 100 * Ngrams[modified_message[j: j+i+1]]

        string = ''
        if key < 10: string = '0'
        key_decryption = 'key = ' + string + str(key) + ': ' + decrypted_message
        DecryptionScores.setdefault(key_decryption, points)

    DecryptionsList = []
    for i in DecryptionScores:
        DecryptionsList.append(i)

    SortedList = QuickSort(DecryptionScores, DecryptionsList)
    TopDecryptions = {}
    for i in SortedList:
        TopDecryptions.setdefault(i, DecryptionScores[i])

    return TopDecryptions