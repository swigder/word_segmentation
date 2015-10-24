from nltk.corpus import gutenberg

from word_segmentation.brown_cmu_unigram_provider import BrownCmuUnigramProvider
from word_segmentation.cmu_dictionary import CmuDictionary
from word_segmentation.globally_optimizing_unigram_word_segmenter import GloballyOptimizingUnigramWordSegmenter
from word_segmentation.globally_optimizing_word_length_maximizing_unigram_word_segmenter import \
    GloballyOptimizingWordLengthMaximizingUnigramWordSegmenter
from word_segmentation.greedy_unigram_word_segmenter import GreedyUnigramWordSegmenter
from word_segmentation.max_match_word_segmenter import MaxMatchWordSegmenter
from word_segmentation.real_word_maximizing_word_segmenter import RealWordMaximizingWordSegmenter


class TestAllWordSegmenters:
    unigram_provider = BrownCmuUnigramProvider()
    cmu_dictionary = CmuDictionary()
    globally_optimizing_unigram_word_segmenter = GloballyOptimizingUnigramWordSegmenter(unigram_provider)
    globally_optimizing_word_length_maximizing_unigram_word_segmenter = \
        GloballyOptimizingWordLengthMaximizingUnigramWordSegmenter(unigram_provider)
    greedy_unigram_word_segmenter = GreedyUnigramWordSegmenter(unigram_provider)
    max_match_word_segmenter = MaxMatchWordSegmenter(cmu_dictionary)
    real_word_maximizing_word_segmenter = RealWordMaximizingWordSegmenter(unigram_provider)

    sentences = gutenberg.sents('bryant-stories.txt')

    def test_all_word_segmenters(self):
        word_segmenters = [
                self.globally_optimizing_unigram_word_segmenter,
                self.globally_optimizing_word_length_maximizing_unigram_word_segmenter,
                self.greedy_unigram_word_segmenter,
                self.max_match_word_segmenter,
                self.real_word_maximizing_word_segmenter
        ]

        errors = {}
        for word_segmenter in word_segmenters:
            errors[word_segmenter] = (0, 0)

        punctuation = ['"', '.', ',', '[', ']', '_', '-', '?', '?"', '."', ',"', '!', '!"']
        for sentence_with_punctuation in self.sentences[10:20]:
            sentence = [segment for segment in sentence_with_punctuation if segment not in punctuation]
            sentence_without_spaces = "".join(sentence)
            for word_segmenter in word_segmenters:
                result = word_segmenter.segment_words(sentence_without_spaces)
                if result != sentence:
                    print(word_segmenter, " ".join(sentence), " ".join(result))
                    sentence_errors, word_errors = errors[word_segmenter]
                    errors[word_segmenter] = (sentence_errors + 1, word_errors + len(set(sentence) ^ set(result)))

        for word_segmenter in word_segmenters:
            print(word_segmenter, errors[word_segmenter])
