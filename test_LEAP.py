from LEAP import *
import unittest



class TestEnum (unittest.TestCase):
    def test_nslookup(self):
        try:
            self.assertIsNone(LocalEnum.ns_lookup(self, "www.google.com"), "142.251.33.196")
        except AssertionError as msg:
            print(msg)
