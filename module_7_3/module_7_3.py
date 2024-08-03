import string
import os


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            words_list = []
            if os.path.isfile(file_name):
                with open(file_name, 'r', encoding='utf-8') as file:
                    for line in file:
                        line = line.lower()
                        line = line.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                        words_list.extend(line.split())
                all_words[file_name] = words_list
            else:
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []

        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word.lower() in words:
                result[file_name] = words.index(word.lower())
            else:
                result[file_name] = None

        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            result[file_name] = words.count(word.lower())

        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('teXT'))
