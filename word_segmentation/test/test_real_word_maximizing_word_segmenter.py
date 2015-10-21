from word_segmentation.real_word_maximizing_word_segmenter import RealWordMaximizingWordSegmenter
from word_segmentation.brown_cmu_unigram_provider import BrownCmuUnigramProvider


class TestRealWordMaximizingWordSegmenter:

    word_segmenter = RealWordMaximizingWordSegmenter(BrownCmuUnigramProvider())

    def test_segment_words(self):
        assert self.word_segmenter.segment_words("there") == ["there"]
        assert self.word_segmenter.segment_words("thetabledownthere") == ["the", "table", "down", "there"]
        assert self.word_segmenter.segment_words("THISISTHESECONDHOMEWORKOFTHEFALLSEMESTER") == \
               ["THIS", "IS", "THE", "SECOND", "HOME", "WORK", "OF", "THE", "FALL", "SEMESTER"]

