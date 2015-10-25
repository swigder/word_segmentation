import argparse
import collections

from word_segmentation.brown_cmu_unigram_provider import BrownCmuUnigramProvider
from word_segmentation.brown_bigram_provider import BrownBigramProvider
from word_segmentation.cmu_dictionary import CmuDictionary
from word_segmentation.bigram_word_segmenter import BigramWordSegmenter
from word_segmentation.globally_optimizing_unigram_word_segmenter import GloballyOptimizingUnigramWordSegmenter
from word_segmentation.globally_optimizing_word_length_maximizing_unigram_word_segmenter import \
    GloballyOptimizingWordLengthMaximizingUnigramWordSegmenter
from word_segmentation.greedy_unigram_word_segmenter import GreedyUnigramWordSegmenter
from word_segmentation.max_match_word_segmenter import MaxMatchWordSegmenter
from word_segmentation.real_word_maximizing_word_segmenter import RealWordMaximizingWordSegmenter

unigram_provider = BrownCmuUnigramProvider()
bigram_provider = BrownBigramProvider()
cmu_dictionary = CmuDictionary()

segmenters = collections.OrderedDict([
    ('bigram', BigramWordSegmenter(unigram_provider, bigram_provider)),
    ('globally_optimizing_unigram', GloballyOptimizingUnigramWordSegmenter(unigram_provider)),
    ('globally_optimizing_word_length_maximizing_unigram',
        GloballyOptimizingWordLengthMaximizingUnigramWordSegmenter(unigram_provider)),
    ('greedy_unigram', GreedyUnigramWordSegmenter(unigram_provider)),
    ('max_match', MaxMatchWordSegmenter(cmu_dictionary)),
    ('real_word_maximizing', RealWordMaximizingWordSegmenter(unigram_provider))
])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Word Segmenter.')

    parser.add_argument('sentence', type=str, help='sentence with no spaces between words')
    segmenter_arg = parser.add_mutually_exclusive_group()
    segmenter_arg.add_argument('-s', '--segmenter', type=str, choices=segmenters.keys(), default='bigram',
                               help='specify a segmenter to use')
    segmenter_arg.add_argument('-a', '--all', action='store_true', help='show results for all segmenters')

    args = parser.parse_args()

    if args.all:
        for segmenter_name, segmenter in segmenters.items():
            print(segmenter_name.ljust(50), ": ", " ".join(segmenter.segment_words(args.sentence)))
    else:
        segmenter = segmenters[args.segmenter]
        print(" ".join(segmenter.segment_words(args.sentence)))
