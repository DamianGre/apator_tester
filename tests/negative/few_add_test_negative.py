import unittest
import clr

clr.AddReference("dlls/PrefixesLib")


from PrefixesLib import PrefixManager


class TestPrefixManager(unittest.TestCase):
    def test_add_returns_zero(self):
        prefix_manager = PrefixManager()
        prefix_manager.Add(16909060, '\x05')
        prefix_manager.Add(16909060, '\x07')
        result = prefix_manager.Add(16909060, '\x07') #added same prefix
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()