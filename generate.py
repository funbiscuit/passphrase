import math
import secrets
import sys

russian_to_english = {
    'а': 'f', 'б': ',', 'в': 'd', 'г': 'u', 'д': 'l', 'е': 't',
    'ё': '`', 'ж': ';', 'з': 'p', 'и': 'b', 'й': 'q', 'к': 'r',
    'л': 'k', 'м': 'v', 'н': 'y', 'о': 'j', 'п': 'g', 'р': 'h',
    'с': 'c', 'т': 'n', 'у': 'e', 'ф': 'a', 'х': '[', 'ц': 'w',
    'ч': 'x', 'ш': 'i', 'щ': 'o', 'ъ': ']', 'ы': 's', 'ь': 'm',
    'э': '\'', 'ю': '.', 'я': 'z'
}

dicts = {
    'adj': 'dict/adj-ru.txt',
    'noun': 'dict/noun-ru.txt',
    'verb': 'dict/verb-ru.txt',
}

max_word_chars = 4


def translate_to_english(russian_text):
    english_text = ''
    for char in russian_text:
        # Translate each character using the dictionary, if possible
        english_text += russian_to_english.get(char, char)
    return english_text


def create_index(filename):
    with open(filename, 'r') as file:
        words = file.readlines()
    words_index = {}

    for word in words:
        key = word.strip()
        if len(key) > max_word_chars:
            key = key[0:max_word_chars]
        translated = translate_to_english(key)
        if translated in words_index:
            words_index[translated].append(word.strip())
        else:
            words_index[translated] = [word.strip()]
    return words_index


def generate_secure_random_int(max_value):
    return secrets.randbelow(max_value + 1)


def random_word(index):
    ind = secrets.randbelow(len(index))
    return index[list(index.keys())[ind]][0]


def main():
    dicts_indices = {}
    for key, filename in dicts.items():
        dicts_indices[key] = create_index(filename)

    # Get all command-line arguments as a single string
    phrase_template = " ".join(sys.argv[1:])
    if len(phrase_template) == 0:
        phrase_template = 'adj noun verb noun'

    phrase = ''
    combinations = 1
    for code in phrase_template.split():
        word = None
        for key, index in dicts_indices.items():
            if code == key:
                word = random_word(index)
                combinations *= len(index)
                break
        if word is None:
            raise ValueError(f'Unknown word type "{code}"')
        phrase = f'{phrase} {word}'.strip()

    password = ''
    for word in phrase.split():
        if len(word) > max_word_chars:
            word = word[0:max_word_chars]
        password = f'{password}{translate_to_english(word)}'

    print(phrase)
    print(password)
    print('Min complexity:', math.floor(math.log2(combinations)), 'bits')
    print('Min complexity:', math.floor(math.log2(combinations) / math.log2(62)), 'chars (a-zA-Z0-9)')


if __name__ == '__main__':
    main()
