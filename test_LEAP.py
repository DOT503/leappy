from LEAP import *
import unittest



class TestEnum (unittest.TestCase):
    def test_nslookup(self):
        self.assertEqual(LocalEnum.ns_lookup(
            self, "www.google.com"), "142.251.33.196")
