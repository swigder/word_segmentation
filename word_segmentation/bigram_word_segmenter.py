from utilities.utilities import bisect_string


class BigramWordSegmenter:
    """
    Segments a sentence containing no spaces into a list of words, by globally maximizing the frequency of words in the
    segmentation as well as favoring longer words.  Each segmentation is given a score, which is the sum of the logs of
    the frequencies of the words divided by the number of words.  Using the log of the frequencies of the words ensures
    that very frequent words, such as "the", don't overwhelm the entire scoring.  In order to favor longer words, and so
    that the addition of logs (a trick to avoid recomputing scores for every combination) does not overwhelmingly favor
    many shorter words over fewer longer words.
    """

    def __init__(self, unigram_provider, bigram_provider):
        """
        :param unigram_provider: unigram provider that can provide the most frequent word of a word list
        """
        self.unigram_provider = unigram_provider
        self.bigram_provider = bigram_provider
        self.total_words = unigram_provider.get_total_words()

    def segment_words(self, string):
        """
        Segments a sentence into words using by optimizing unigram counts globally as well as favoring long words over
        short ones.
        :param string: words without spaces separating them
        :return: list of words that are a word segmentation of the given string
        """
        segmentation, frequency = self.segment_words_dynamically(string, {})
        return segmentation

    def segment_words_dynamically(self, string, cache):
        """
        Segments a sentence into words using by optimizing unigram counts globally as well as favoring long words over
        short ones. Uses dynamic programming under the hood, adding to the cache of best segmentation for the given
        string and all substrings.
        This method is called recursively.
        :param string: words without spaces separating them
        :param cache: cache of best segmentations for the string (or any other strings in the global string)
        :return: list of words that are a word segmentation of the given string
        """
        if string in cache:  # dynamic programming part
            return cache[string]

        probability_whole = self.unigram_provider.get_frequency(string) / self.total_words
        if len(string) <= 1:  # base case
            cache[string] = [string], probability_whole
            return cache[string]

        best_segmentation = [string]
        best_score = probability_whole

        for i in range(1, len(string)):  # recursive case
            a, b = bisect_string(string, i)
            segmentation_a, score_a = self.segment_words_dynamically(a, cache)
            segmentation_b, score_b = self.segment_words_dynamically(b, cache)
            new_bigram = tuple([segmentation_a[-1], segmentation_b[0]])
            frequency_first_word = max(self.unigram_provider.get_frequency(segmentation_a[-1]), 1)
            probability_new_bigram = max(1, self.bigram_provider.get_frequency(new_bigram)) / frequency_first_word
            score = score_a * score_b * probability_new_bigram
            if score > best_score:
                best_score = score
                best_segmentation = segmentation_a + segmentation_b

        cache[string] = best_segmentation, best_score
        return cache[string]
