from utilities.utilities import bisect_string
from math import exp, log


class GloballyOptimizingUnigramWordSegmenter:
    """
    Segments a sentence containing no spaces into a list of words, by globally maximizing the frequency of words in the
    segmentation as well as favoring longer words.  Each segmentation is given a score, which is the sum of the logs of
    the frequencies of the words divided by the number of words.  Using the log of the frequencies of the words ensures
    that very frequent words, such as "the", don't overwhelm the entire scoring.  In order to favor longer words, and so
    that the addition of logs (a trick to avoid recomputing scores for every combination) does not overwhelmingly favor
    many shorter words over fewer longer words.
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
        score_whole = log(frequency_whole) if frequency_whole != 0 else 0
        if len(string) <= 1:  # base case
            cache[string] = [string], score_whole
            return cache[string]

        best_segmentation = [string]
        best_score = score_whole

        for i in range(1, len(string)):  # recursive case
            a, b = bisect_string(string, i)
            segmentation_a, score_a = self.segment_words_dynamically(a, cache)
            segmentation_b, score_b = self.segment_words_dynamically(b, cache)
            score = log(exp(score_a) + exp(score_b)) / (len(segmentation_a) + len(segmentation_b))
            if score > best_score:
                best_score = score
                best_segmentation = segmentation_a + segmentation_b

        cache[string] = best_segmentation, best_score
        return cache[string]
