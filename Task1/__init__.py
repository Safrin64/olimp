filepath = input('Введите путь к файлу: \n')

test = open(filepath)


encoding = [
    'utf-8',
    'cp10007',
    'cp1251',
    'KOI8R',
    'ISO-8859-5',
    'cp866',
]

correct_encoding = ''

for enc in encoding:
    try:
        file = open(filepath, encoding=enc).read()
        print(file)

    except (UnicodeDecodeError, LookupError):
        pass

    else:
        correct_encoding = enc
        break
print(correct_encoding)