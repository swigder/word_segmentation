from word_segmentation.globally_optimizing_word_length_maximizing_unigram_word_segmenter import GloballyOptimizingWordLengthMaximizingUnigramWordSegmenter
from word_segmentation.brown_cmu_unigram_provider import BrownCmuUnigramProvider


class TestGloballyOptimzingUnigramWordSegmenter:

    word_segmenter = GloballyOptimizingWordLengthMaximizingUnigramWordSegmenter(BrownCmuUnigramProvider())

    def test_segment_words(self):
        assert self.word_segmenter.segment_words("there") == ["there"]
        assert self.word_segmenter.segment_words("thetabledownthere") == ["the", "table", "down", "there"]
        assert self.word_segmenter.segment_words("THISISTHESECONDHOMEWORKOFTHEFALLSEMESTER") == \
               ["THIS", "IS", "THE", "SECOND", "HOMEWORK", "OF", "THE", "FALL", "SEMESTER"]

