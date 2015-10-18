from word_segmentation.max_match_word_segmenter import MaxMatchWordSegmenter
from word_segmentation.cmu_dictionary import CmuDictionary


class TestMaxMatcher:

    max_matcher = MaxMatchWordSegmenter(CmuDictionary())

    def test_segment_words(self):
        assert self.max_matcher.segment_words("there") == ["there"]
        assert self.max_matcher.segment_words("thetabledownthere") == ["theta", "bled", "own", "there"]
        assert self.max_matcher.segment_words("THISISTHESECONDHOMEWORKOFTHEFALLSEMESTER") == \
               ["THIS", "IS", "THESE", "CON", "D", "HOMEWORK", "OFT", "HE", "FALLS", "EM", "ESTER"]

