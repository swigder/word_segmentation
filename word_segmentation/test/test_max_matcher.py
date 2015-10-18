from word_segmentation.max_matcher import MaxMatcher
from word_segmentation.cmu_dictionary import CmuDictionary


class TestMaxMatcher:

    max_matcher = MaxMatcher(CmuDictionary())

    def test_max_match(self):
        assert self.max_matcher.max_match("thetabledownthere") == ["theta", "bled", "own", "there"]
        assert self.max_matcher.max_match("THISISTHESECONDHOMEWORKOFTHEFALLSEMESTER") == \
               ["THIS", "IS", "THESE", "CON", "D", "HOMEWORK", "OFT", "HE", "FALLS", "EM", "ESTER"]

