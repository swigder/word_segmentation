from word_segmentation.unigram_word_segmenter import UnigramWordSegmenter
from word_segmentation.brown_unigram_provider import BrownUnigramProvider


class TestMaxMatcher:

    word_segmenter = UnigramWordSegmenter(BrownUnigramProvider())

    def test_max_match(self):
        assert self.word_segmenter.segment_words("there") == ["the", "re"]
        assert self.word_segmenter.segment_words("thetabledownthere") == ["the", "table", "do", "w", "n", "the", "re"]
        assert self.word_segmenter.segment_words("THISISTHESECONDHOMEWORKOFTHEFALLSEMESTER") == \
               ["THIS", "IS", "THE", "SECOND", "HOME", "WORK", "OF", "THE", "FALL", "SEMESTER"]

