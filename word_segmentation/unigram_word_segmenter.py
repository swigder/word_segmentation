class UnigramWordSegmenter:
    """
    Segments a sentence containing no spaces into a list of words, by greedily maximizing the unigram counts for each
    possible word from left-to-right.  Unigram counts are provided by a given unigram_provider.
    While this algorithm far better than the max-match word segmentation algorithm for English, it still leaves much
    to be desired.  For example, it will always segment "there" as ["the", "re"] because of "the"'s overwhelming word
    frequency.
    """

    def __init__(self, unigram_provider):
        """
        :param unigram_provider: unigram provider that can provide the most frequent word of a word list
        """
        self.unigram_provider = unigram_provider

    def segment_words(self, string):
        """
        Segments a sentence into words using a greedy word-frequency maximizing algorithm.  This will attempt to
        greedily find the most frequent possible of possible words on at a time, starting at the beginning and moving
        left-to-right with the remaining string.
        :param string: words without spaces separating them
        :return: list of words that are a word segmentation of the given string
        """
        words = []

        word_begin = 0
        while word_begin < len(string):
            word_options = self.find_prefixes(string[word_begin:])
            if len(word_options) > 0:
                best_word = self.unigram_provider.get_most_frequent_word(word_options)
            else:
                best_word = string[word_begin:word_begin+1]
            words.append(best_word)
            word_begin += len(best_word)

        return words

    def find_prefixes(self, string):
        words = []
        word_end = len(string)
        while word_end > 1:
            test_word = string[:word_end]
            if self.unigram_provider.get_frequency(test_word) > 0:
                words.append(test_word)
            word_end -= 1
        return words

