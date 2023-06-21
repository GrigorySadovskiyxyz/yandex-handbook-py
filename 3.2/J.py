import string
zamena = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TC',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ы': 'Y',
    'Э': 'E',
    'Ю': 'IU',
    'Я': 'IA',
    'Ё': 'E',
    'Й': 'I',
    'Ъ': '',
    'Ь': ''
}

n = [*input()]
result = ''
for char in n:
    if char == char.upper():
        if char not in zamena:
            result += char
        elif len(zamena[char]) > 1:
            result += string.capwords(zamena[char])
        else:
            result += zamena[char]
    elif char == char.lower():
        if char.upper() not in zamena:
            result += char
        else:
            result += zamena[char.upper()].lower()
print(result)
