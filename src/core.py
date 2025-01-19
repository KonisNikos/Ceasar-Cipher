english_str = 'abcdefghijklmnopqrstuvwxyz'
english_dict = {'a': 0 , 'b': 1 , 'c': 2 , 'd': 3 , 'e': 4 , 'f': 5 , 'g': 6 , 'h': 7 , 'i': 8 ,
                'j': 9 , 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
                's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
ENGLISH_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ENGLISH_dict = {'A': 0 , 'B': 1 , 'C': 2 , 'D': 3 , 'E': 4 , 'F': 5 , 'G': 6 , 'H': 7 , 'I': 8 ,
                'J': 9 , 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
                'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

greek_str = 'αβγδεζηθικλμνξοπρστυφχψω'
greek_dict = {'α': 0 , 'β': 1 , 'γ': 2 , 'δ': 3 , 'ε': 4 , 'ζ': 5 , 'η': 6 , 'θ': 7 , 'ι': 8 , 'κ': 9 , 'λ': 10, 'μ': 11,
              'ν': 12, 'ξ': 13, 'ο': 14, 'π': 15, 'ρ': 16, 'σ': 17, 'τ': 18, 'υ': 19, 'φ': 20, 'χ': 21, 'ψ': 22, 'ω': 23,
              'ά': 0 , 'έ': 4 , 'ή': 6 , 'ί': 8 , 'ϊ': 8 , 'ΐ': 8 , 'ό': 14, 'ς': 17, 'ύ': 19, 'ϋ': 19, 'ΰ': 19, 'ώ': 23}
GREEK_str = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
GREEK_dict = {'Α': 0 , 'Β': 1 , 'Γ': 2 , 'Δ': 3 , 'Ε': 4 , 'Ζ': 5 , 'Η': 6 , 'Θ': 7 , 'Ι': 8 , 'Κ': 9 , 'Λ': 10,
              'Μ': 11, 'Ν': 12, 'Ξ': 13, 'Ο': 14, 'Π': 15, 'Ρ': 16, 'Σ': 17, 'Τ': 18, 'Υ': 19, 'Φ': 20, 'Χ': 21,
              'Ψ': 22, 'Ω': 23, 'Ά': 0 , 'Έ': 4 , 'Ή': 6 , 'Ί': 8 , 'Ϊ': 8 , 'Ό': 14, 'Ύ': 19, 'Ϋ': 19, 'Ώ': 23}

symbol_str = '''~`!1@2#3$4€%5^6&7*8(9)0_-+={[}]|:;"'<,>.?/ '''
symbol_dict = {'~': 0 , '`': 1 , '!': 2 , '1': 3 , '@': 4 , '2': 5 , '#': 6 , '3': 7 , '$': 8 , '4': 9 , '€': 10, '%': 11, '5': 12, '^': 13, '6': 14,
               '&': 15, '7': 16, '*': 17, '8': 18, '(': 19, '9': 20, ')': 21, '0': 22, '_': 23, '-': 24, '+': 25, '=': 26, '{': 27, '[': 28, '}': 29,
               ']': 30, '|': 31, ':': 32, ';': 33, '"': 34, "'": 35, '<': 36, ',': 37, '>': 38, '.': 39, '?': 40, '/': 41, ' ': 42}


def encode(plain_text: str, key: int, Toggles: list, characters = ''):

    if not isinstance(plain_text, str):
        raise TypeError(f"Expected a str, got {type(plain_text).__name__}")
    if not isinstance(key, int):
        raise TypeError(f"Expected an int, got {type(key).__name__}")
    if not isinstance(Toggles, list):
        raise TypeError(f"Expected a list, got {type(Toggles).__name__}")
    if len(Toggles) != 4:
        raise ValueError(f"Expected 4 items in list, got {len(Toggles)}")
    for i in Toggles:
        if not isinstance(i, bool):
            raise TypeError(f"Expected a bool, got {type(i).__name__}")
    if Toggles[3]:
        if not isinstance(characters, str):
            raise TypeError(f"Expected a str, got {type(characters).__name__}")
        for i in range(len(characters)):
            if i < len(characters)-1 and characters[i] in characters[i+1:]:
                raise ValueError(f"Expected only unique characters, got {characters[i]} multiple times")

    if Toggles[3]:
        characters_dict = {}
        for i in range(len(characters)):
            characters_dict.setdefault(characters[i], i)

    cipher_text = ''
    for i in plain_text:

        if Toggles[3]:
            if i in characters:
                cipher_text += characters[(characters_dict[i] - key) % len(characters)]
            else:
                cipher_text += i
            continue

        elif Toggles[0] and i in english_str:
            cipher_text += english_str[(english_dict[i] - key) % 26]
        elif Toggles[0] and i in ENGLISH_str:
            cipher_text += ENGLISH_str[(ENGLISH_dict[i] - key) % 26]

        elif Toggles[1] and i in greek_dict:
            cipher_text += greek_str[(greek_dict[i] - key) % 24]
        elif Toggles[1] and i in GREEK_dict:
            cipher_text += GREEK_str[(GREEK_dict[i] - key) % 24]

        elif Toggles[2] and i in symbol_str:
            cipher_text += symbol_str[(symbol_dict[i] - key) % 43]

        else:
            cipher_text += i

    return cipher_text


def decode(cipher_text: str, key: int, Toggles: list, characters = ''):

    return encode(cipher_text, -key, Toggles, characters)


def BruteForce(cipher_text: str, Toggles: list, characters = ''):

    if not isinstance(Toggles, list):
        raise TypeError(f"Expected a list, got {type(Toggles).__name__}")
    if len(Toggles) != 4:
        raise ValueError(f"Expected 4 items in list, got {len(Toggles)}")
    for i in (Toggles):
        if not isinstance(i, bool):
            raise TypeError(f"Expected a bool, got {type(i).__name__}")
    if Toggles[3] and not isinstance(characters, str):
        raise TypeError(f"Expected a str, got {type(characters).__name__}")

    if Toggles[0]:
        max_key = 26
    elif Toggles[1]:
        max_key = 24
    elif Toggles[2]:
        max_key = 43    
    elif Toggles[3]:
        max_key = len(characters)

    PossibleDecryptions = {}
    for key in range(max_key):
        if key < 10:
            str_key = '0' + str(key)
        else:
            str_key = str(key)
        PossibleDecryptions.setdefault(decode(cipher_text, key, Toggles, characters), str_key)

    return PossibleDecryptions


# The following N-grams are the most common, taken from their respective wikipedia page (if it exists)
# and/or from the site: https://www3.nd.edu/~busiforc/handouts/cryptography/Letter%20Frequencies.html
Bigrams = {'th':2, 'he':2, 'in':2, 'er':2, 'an':2, 're':2, 'on':2, 'at':2, 'en':2, 'nd':2, 'ti':2, 'es':2, 'or':2, 'te':2, 'of':2, 'ed':2, 'is':2, 'it':2, 'al':2, 'ar':2, 'st':2,
           'to':1, 'nt':1, 'ng':1, 'se':1, 'ha':1, 'as':1, 'ou':1, 'io':1, 'le':1, 've':1, 'co':1, 'me':1, 'de':1, 'hi':1, 'ri':1, 'ro':1, 'ic':1, 'ne':1, 'ea':1, 'ra':1, 'ce':1}

Trigrams = {'the':5, 'and':5, 'ing':5, 'her':5, 'hat':5, 'his':5, 'tha':5, 'ere':5, 'for':5, 'ent':5, 'ion':5, 'ter':5, 'was':5, 'you':5,
            'ith':4, 'ver':4, 'all':4, 'wit':4, 'thi':4, 'tio':4, 'nde':4, 'has':4, 'nce':4, 'edt':4, 'tis':4, 'oft':4, 'sth':4, 'men':4}

Quadrigrams = {'that':6, 'ther':6, 'with':6, 'tion':6, 'here':6, 'ould':6, 'ight':6, 'have':6, 'hich':6, 'whic':6,
               'this':6, 'thin':6, 'they':6, 'atio':6, 'ever':6, 'from':6, 'ough':6, 'were':6, 'hing':6, 'ment':6}


def QuickSort(List: list):
    if len(List) < 2: return List
    i = 0
    for j in range(len(List)-1):
        if List[j][2] > List[-1][2]:
            List[i], List[j] = List[j], List[i]
            i += 1
    List[i], List[-1] = List[-1], List[i]

    Left = QuickSort(List[:i])
    Right = QuickSort(List[i+1:])

    return Left + [List[i]] + Right


def AutoDecrypt(cipher_text: str, Toggles: list, characters = ''):

    if not isinstance(Toggles, list):
        raise TypeError(f"Expected a list, got {type(Toggles).__name__}")
    if len(Toggles) != 4:
        raise ValueError(f"Expected 4 items in list, got {len(Toggles)}")
    for i in (Toggles[0], Toggles[3]):
        if not isinstance(i, bool):
            raise TypeError(f"Expected a bool, got {type(i).__name__}")

    PossibleDecryptions = BruteForce(cipher_text, Toggles, characters)
    DecryptionList = []

    for decrypted_message in PossibleDecryptions:
        key = PossibleDecryptions[decrypted_message]
        points = 0

        modified_message = ''
        for i in decrypted_message:
            if i in ENGLISH_str:
                modified_message += english_str[ENGLISH_dict[i]]
                points -= 1
            else:
                modified_message += i

        for i in range(1, 4):
            Ngrams = [Bigrams, Trigrams, Quadrigrams][i-1]
            for j in range(len(modified_message)-i):
                if modified_message[j: j+i+1] in Ngrams:
                    points += 100 * Ngrams[modified_message[j: j+i+1]]

        DecryptionList.append({0:key, 1:decrypted_message, 2:points})

    SortedList = QuickSort(DecryptionList)

    return SortedList