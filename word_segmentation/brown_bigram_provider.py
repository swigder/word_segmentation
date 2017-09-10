from nltk.corpus import brown
import nltk

from utilities.space_efficient_dict import SpaceEfficientDict


class BrownBigramProvider:
    """
    Provides bigram counts for words in the Brown corpus.  Keeps corpus in memory for speed.
    """

    def __init__(self, space_optimize=False):
        """
        :param space_optimize: Set to True to optimize for space. This will cause significantly longer initialization
        and slightly longer reads.
        """
        if not space_optimize:
            brown_sentences = [[word.lower() for word in sent] for sent in brown.sents()]
            bigrams = [bigram for elem in [list(nltk.bigrams(sent)) for sent in brown_sentences] for bigram in elem]
            self.bigram_distributions = nltk.FreqDist(bigrams)
        else:
            self.bigram_distributions = SpaceEfficientDict()
            for sent in brown.sents():
                lower_sent = [word.lower() for word in sent]
                for bigram in nltk.bigrams(lower_sent):
                    self.bigram_distributions.increment(bigram)

    def get_frequency(self, bigram):
        """
        Gets the absolute count of a given bigram in the Brown corpus.  These counts are case-insensitive.
        :param bigram: bigram tuple to find in the corpus
        :return: number of times the bigram appears in the corpus, ignoring letter case
        """
        return self.bigram_distributions[tuple([word.lower() for word in bigram])]

    def get_total_bigrams(self):
        return len(self.bigram_distributions)
