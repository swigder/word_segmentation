from word_segmentation.greedy_unigram_word_segmenter import GreedyUnigramWordSegmenter
from word_segmentation.brown_cmu_unigram_provider import BrownCmuUnigramProvider


class TestGreedyUnigramWordSegmenter:

    word_segmenter = GreedyUnigramWordSegmenter(BrownCmuUnigramProvider())

    def test_segment_words(self):
        assert self.word_segmenter.segment_words("there") == ["the", "re"]
        assert self.word_segmenter.segment_words("thetabledownthere") == ["the", "table", "do", "w", "n", "the", "re"]
        assert self.word_segmenter.segment_words("THISISTHESECONDHOMEWORKOFTHEFALLSEMESTER") == \
               ["THIS", "IS", "THE", "SECOND", "HOME", "WORK", "OF", "THE", "FALL", "SEMESTER"]

