from LEAP import *
import unittest



class TestEnum (unittest.TestCase):
    def test_nslookup(self):
        try:
            self.assertIsNone(LocalEnum.ns_lookup(self, "www.google.com"), "142.251.33.196")
        except AssertionError as msg:
            print(msg)
    def test_get_system_user_list(self):
        try:
            self.assertIsNone(LocalEnum.get_system_user_list(self), "result")
        except AssertionError as msg:
            print(msg)
    def test_elevate(self):
        try:
            self.assertIsNone(LocalEnum.get_system_user_list(self), 0)
        except AssertionError as msg:
            print(msg)
