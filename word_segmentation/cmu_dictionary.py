from nltk.corpus import cmudict


class CmuDictionary:

    words = cmudict.words()

    def is_word(self, word):
        return word.lower() in self.words
