import sys

letters = {
    'א': 't',
    'ב': 'c',
    'ג': 'd',
    'ד': 's',
    'ה': 'v',
    'ו': 'u',
    'ז': 'z',
    'ח': 'j',
    'ט': 'y',
    'י': 'h',
    'כ': 'f',
    'ל': 'k',
    'מ': 'n',
    'נ': 'b',
    'ס':  'x',
    'ע':  'g',
    'פ':  'y',
    'צ':  'h',
    'ק':  'e',
    'ר':  'k',
    'ש':  'n',
    'ת':  'b',
    '.': '/',
    'ץ': '.',
    'ם': 'o',
    'ן': 'i',
    'ף': ';',
    'ך': 'l',
}


words = sys.argv[1:]
result = ''
for word in words:
    new_word = ''
    for letter in word:
        if letter in letters:
            new_word += letters[letter]
        else:
            new_word += letter
    result += new_word + ' '


print(result)
