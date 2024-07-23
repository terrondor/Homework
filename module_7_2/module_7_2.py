def custom_write(file_name, strings):
    string_position = {}
    f = open(file_name, 'w', encoding='utf-8')

    for i, line in enumerate(strings, start=1):
        start_byte_position = f.tell()
        f.write(line + '\n')
        string_position[(i, start_byte_position)] = line

    f.close()

    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
