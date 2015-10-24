from word_segmentation.bigram_word_segmenter import BigramWordSegmenter
from word_segmentation.brown_bigram_provider import BrownBigramProvider
from word_segmentation.brown_cmu_unigram_provider import BrownCmuUnigramProvider


class TestBigramWordSegmenter:

    word_segmenter = BigramWordSegmenter(BrownCmuUnigramProvider(), BrownBigramProvider())

    def test_segment_words(self):
        assert self.word_segmenter.segment_words("there") == ["there"]
        assert self.word_segmenter.segment_words("thetabledownthere") == ["the", "table", "down", "there"]
        assert self.word_segmenter.segment_words("THISISTHESECONDHOMEWORKOFTHEFALLSEMESTER") == \
               ["THIS", "IS", "THE", "SECOND", 'HOMEWORK', "OF", "THE", "FALL", "SEMESTER"]

