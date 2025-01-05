alpha = 'abcdefghijklmnopqrstuvwxyz'
abc_dict = {'a': 0 , 'b': 1 , 'c': 2 , 'd': 3 , 'e': 4 , 'f': 5 , 'g': 6 , 'h': 7 , 'i': 8 ,
            'j': 9 , 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
            's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ABC_dict = {'A': 0 , 'B': 1 , 'C': 2 , 'D': 3 , 'E': 4 , 'F': 5 , 'G': 6 , 'H': 7 , 'I': 8 ,
            'J': 9 , 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
            'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

αλφα = 'αβγδεζηθικλμνξοπρστυφχψω'
αβγ_dict = {'α': 0 , 'β': 1 , 'γ': 2 , 'δ': 3 , 'ε': 4 , 'ζ': 5 , 'η': 6 , 'θ': 7 , 'ι': 8 , 'κ': 9 , 'λ': 10, 'μ': 11,
            'ν': 12, 'ξ': 13, 'ο': 14, 'π': 15, 'ρ': 16, 'σ': 17, 'τ': 18, 'υ': 19, 'φ': 20, 'χ': 21, 'ψ': 22, 'ω': 23,
            'ά': 0 , 'έ': 4 , 'ή': 6 , 'ί': 8 , 'ϊ': 8 , 'ΐ': 8 , 'ό': 14, 'ς': 17, 'ύ': 19, 'ϋ': 19, 'ΰ': 19, 'ώ': 23}
ΑΛΦΑ = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
ΑΒΓ_dict = {'Α': 0 , 'Β': 1 , 'Γ': 2 , 'Δ': 3 , 'Ε': 4 , 'Ζ': 5 , 'Η': 6 , 'Θ': 7 , 'Ι': 8 , 'Κ': 9 , 'Λ': 10,
            'Μ': 11, 'Ν': 12, 'Ξ': 13, 'Ο': 14, 'Π': 15, 'Ρ': 16, 'Σ': 17, 'Τ': 18, 'Υ': 19, 'Φ': 20, 'Χ': 21,
            'Ψ': 22, 'Ω': 23, 'Ά': 0 , 'Έ': 4 , 'Ή': 6 , 'Ί': 8 , 'Ϊ': 8 , 'Ό': 14, 'Ύ': 19, 'Ϋ': 19, 'Ώ': 23}

# TODO: Add a preview of the syms string below to show which and how the characters will rotate.
syms = '''~`!1@2#3$4€%5^6&7*8(9)0_-+={[}]|:;"'<,>.?/ '''
sym_dict = {'~': 0 , '`': 1 , '!': 2 , '1': 3 , '@': 4 , '2': 5 , '#': 6 , '3': 7 , '$': 8 , '4': 9, '€': 10, '%': 11, '5': 12, '^': 13, '6': 14,
            '&': 15, '7': 16, '*': 17, '8': 18, '(': 19, '9': 20, ')': 21, '0': 22, '_': 23, '-': 24, '+': 25, '=': 26, '{': 27, '[': 28,
            '}': 29, ']': 30, '|': 31, ':': 32, ';': 33, '"': 34, "'": 35, '<': 36, ',': 37, '>': 38, '.': 39, '?': 40, '/': 41, ' ': 42}


# TODO: Add toggles to the UI for the options: English, Greek, Symbols and Numbers, Custom.
# TODO: Do not run if no toggle is chosen and show a respective message.
# TODO: Custom should disable all other toggles (on UI as well).
# TODO: Ask for unique characters as a string and assign the given string to "characters" below.
def encode(plain_text: str, key: int, English: bool, Greek: bool, Symbols: bool, Custom: bool, characters: str):

    if not isinstance(plain_text, str):
        raise TypeError(f"Expected a str, got {type(plain_text).__name__}")
    if not isinstance(key, int):
        raise TypeError(f"Expected an int, got {type(key).__name__}")
    for i in (English, Greek, Symbols, Custom):
        if not isinstance(i, bool):
            raise TypeError(f"Expected an int, got {type(i).__name__}")
    if Custom and not isinstance(characters, str):
        raise TypeError(f"Expected a str, got {type(characters).__name__}")

    if Custom:
        cha_dict = {}
        for i in range(len(characters)):
            if i in cha_dict:
                # TODO: Return an error saying that every character should be unique and showing the problematic character.
                pass
                ...
        cha_dict.setdefault(characters[i], i)

    cipher_text = ''
    for i in plain_text:

        if Custom:
            if i in cha_dict:
                cipher_text += characters[(cha_dict[i] - key) % len(characters)]
            else:
                cipher_text += i
            continue

        elif English and i in alpha:
            cipher_text += alpha[(abc_dict[i] - key) % 26]
        elif English and i in ALPHA:
            cipher_text += ALPHA[(ABC_dict[i] - key) % 26]

        elif Greek and i in αβγ_dict:
            cipher_text += αλφα[(αβγ_dict[i] - key) % 24]
        elif Greek and i in ΑΒΓ_dict:
            cipher_text += ΑΛΦΑ[(ΑΒΓ_dict[i] - key) % 24]

        elif Symbols and i in syms:
            cipher_text += syms[(sym_dict[i] - key) % 43]

        else:
            cipher_text += i

    return cipher_text


def decode(cipher_text: str, key: int, English: bool, Greek: bool, Symbols: bool, Custom: bool, characters: str):

    return encode(cipher_text, -key, English, Greek, Symbols, Custom, characters)


# TODO: Add a disclaimer when choosing this function stating the below.
# Only usable with one toggle on!
def BruteForce(cipher_text: str, English: bool, Greek: bool, Symbols: bool, Custom: bool, characters: str):

    if not isinstance(cipher_text, str):
        raise TypeError(f"Expected a str, got {type(cipher_text).__name__}")

    if English:
        max = 26
    elif Greek:
        max = 24
    elif Symbols:
        max = 43    
    elif Custom:
        max = len(characters)

    Dict = {}
    for key in range(max):
        Dict.setdefault(decode(cipher_text, key, English, Greek, Symbols, Custom, characters), key)
    return Dict


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
# Only works for english decryption! Use with english or custom ciphers.
def AutoDecrypt(cipher_text: str, English: bool, Custom: bool, characters: str):

    if not isinstance(cipher_text, str):
        raise TypeError(f"Expected a str, got {type(cipher_text).__name__}")
    for i in(English, Custom):
        if not isinstance(i, bool):
            raise TypeError(f"Expected an int, got {type(i).__name__}")
    if Custom and not isinstance(characters, str):
        raise TypeError(f"Expected a str, got {type(characters).__name__}")

    Dict = BruteForce(cipher_text, English, False, False, Custom, characters)
    DecryptionScores = {}

    for decrypted_message in Dict:
        key = Dict[decrypted_message]
        points = 0

        modified_message = ''
        for i in decrypted_message:
            if i in ALPHA:
                modified_message += alpha[ABC_dict[i]]
            else:
                modified_message += i

        for i in range(1, 4):
            Ngrams = [Bigrams, Trigrams, Quadrigrams][i-1]
            for j in range(len(modified_message)-i):
                if modified_message[j: j+i+1] in Ngrams:
                    points += Ngrams[modified_message[j: j+i+1]]

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