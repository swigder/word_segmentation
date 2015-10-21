from utilities.utilities import bisect_string
from math import pow


class GloballyOptimizingWordLengthMaximizingUnigramWordSegmenter:
    """
    Segments a sentence containing no spaces into a list of words, by globally maximizing the frequency of words in the
    segmentation as well as favoring longer words.  Each segmentation is given a score, which is the product of the
    frequency of the word and the power of the length of the word.  Using the power of the length of the word ensures
    that less frequent compound words have a chance against their more frequent counterparts (such as "homework" against
    "home", "work"), but even is necessary to ensure that very frequent words, such as "the", don't overwhelm the entire
    scoring.  (Tests using the log of the frequency to avoid this overwhelming effect ran into the same problem by for
    a different reason -- adding logs favors many small words over longer ones, and recomputing the frequencies after
    adjusting for word length is expensive and non-trivial.)
    """

    def __init__(self, unigram_provider):
        """
        :param unigram_provider: unigram provider that can provide the most frequent word of a word list
        """
        self.unigram_provider = unigram_provider

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

        frequency_whole = self.unigram_provider.get_frequency(string)
        score_whole = frequency_whole * pow(len(string), 11)
        if len(string) <= 1:  # base case
            cache[string] = [string], score_whole
            return cache[string]

        best_segmentation = [string]
        best_score = score_whole

        for i in range(1, len(string)):  # recursive case
            a, b = bisect_string(string, i)
            segmentation_a, score_a = self.segment_words_dynamically(a, cache)
            segmentation_b, score_b = self.segment_words_dynamically(b, cache)
            score = score_a + score_b
            if score > best_score:
                best_score = score
                best_segmentation = segmentation_a + segmentation_b

        cache[string] = best_segmentation, best_score
        return cache[string]
