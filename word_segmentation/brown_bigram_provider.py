from nltk.corpus import brown
import nltk


class BrownBigramProvider:
    """
    Provides bigram counts for words in the Brown corpus.  Keeps corpus in memory for speed.
    """

    brown_sentences = [[word.lower() for word in sent] for sent in brown.sents()]
    bigrams = [bigram for elem in [list(nltk.bigrams(sent)) for sent in brown_sentences] for bigram in elem]
    bigram_distributions = nltk.FreqDist(bigrams)

    def get_frequency(self, bigram):
        """
        Gets the absolute count of a given bigram in the Brown corpus.  These counts are case-insensitive.
        :param bigram: bigram tuple to find in the corpus
        :return: number of times the bigram appears in the corpus, ignoring letter case
        """
        return self.bigram_distributions[tuple([word.lower() for word in bigram])]

    def get_total_bigrams(self):
        return len(self.bigrams)
