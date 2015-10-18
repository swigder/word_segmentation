from nltk.corpus import brown
import nltk


class BrownUnigramProvider:
    """
    Provides unigram counts for words in the Brown corpus.  Keeps corpus in memory for speed.
    """

    words = brown.words()
    word_distribution = nltk.FreqDist(w.lower() for w in words)

    def get_frequency(self, word):
        """
        Gets the absolute count of a given word in the Brown corpus.  These counts are case-insensitive.
        :param word: word to find in the corpus
        :return: number of times the word appears in the corpus, ignoring letter case
        """
        return self.word_distribution[word.lower()]

    def get_most_frequent_word(self, words):
        """
        Finds the word in a list of words with the highest frequency in the Brown corpus (using rules of get_frequency)
        :param words: list of words for which to find the word with the highest frequency
        :return: word in the list with the high
        """
        return max(words, key=lambda word: self.get_frequency(word))
