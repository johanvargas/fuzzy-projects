from unittest import TestCase
import htmlscrap as html_scrapper

class TryTesting(TestCase):

    def test_always_passes(self):
        assert True

#    def test_always_fails(self):
#        assert False

    def test_other_vals(self):
        hs = html_scrapper
        assert(hs)
