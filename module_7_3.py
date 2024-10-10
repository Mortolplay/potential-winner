class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = file_name
        self.file_names = [*file_name]

    def get_all_words(self):
        all_words = {}
        words = []
        for chto in self.file_names:
            with open(chto, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for i in line:
                        if i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            line = line.replace(i, '')
                    a = line.split()
                    for v in a:
                        words.append(v)
                all_words[self.file_name] = words
                return all_words

    def find(self, word):
        m = {}
        for name, words in self.get_all_words().items():
            for i in words:
                if word.lower() == i:
                    m[self.file_name] = words.index(i)
        return m
    def count(self, word):
        c = {}
        x = 0
        for name, words in self.get_all_words().items():
            for i in words:
                if word.lower() == i:
                    x = x + 1
                    c[self.file_name] = x
        return c
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
