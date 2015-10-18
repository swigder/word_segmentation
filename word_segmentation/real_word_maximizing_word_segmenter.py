from utilities.utilities import bisect_string


class RealWordMaximizingWordSegmenter:
    """
    Segments a sentence containing no spaces into a list of words, by globally maximizing the proportion of words to
    non-words in the segmentation.  Each segmentation is given a score, which is the sum of a positive point value for
    each word whose unigram count is higher than some threshold, and higher negative point value for each word whose
    unigram count is below that threshold.  The constant scores and high negative : positive score ratio was required
    to ensure that short, extremely frequent words don't overwhelm less common words.
    This algorithm has the limitation that it will always favor two shorter real words instead of one longer one.  For
    example, ["home", "work"] will always be favored over ["homework"]
    """

    SCORE_WORD = 1
    PENALTY_NON_WORD = -3
    WORD_THRESHOLD = 100

    def __init__(self, unigram_provider):
        """
        :param unigram_provider: unigram provider that can provide the most frequent word of a word list
        """
        self.unigram_provider = unigram_provider

    def segment_words(self, string):
        """
        Segments a sentence into words using a globally optimal real:fake word ratio maximizing algorithm.
        :param string: words without spaces separating them
        :return: list of words that are a word segmentation of the given string
        """
        segmentation, frequency = self.segment_words_dynamically(string, {})
        return segmentation

    def segment_words_dynamically(self, string, cache):
        """
        Segments a sentence into words using a globally optimal real:fake word ratio maximizing algorithm.  Uses dynamic
        programming under the hood, adding to the cache of best segmentation for the given string and all substrings.
        This method is called dynamically.
        :param string: words without spaces separating them
        :param cache: cache of best segmentations for the string (or any other strings in the global string)
        :return: list of words that are a word segmentation of the given string
        """
        if string in cache:  # dynamic programming part
            return cache[string]

        frequency_whole = self.unigram_provider.get_frequency(string)
        score_whole = self.SCORE_WORD if frequency_whole > self.WORD_THRESHOLD else self.PENALTY_NON_WORD
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
