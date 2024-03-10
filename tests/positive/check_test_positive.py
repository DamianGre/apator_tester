import unittest
import clr

clr.AddReference("dlls/PrefixesLib")


from PrefixesLib import PrefixManager


class TestPrefixManager(unittest.TestCase):
    def test_add_returns_zero(self):
        prefix_manager = PrefixManager()
        prefix_manager.Add(16909060, ' ')
        prefix_manager.Add(16909060, '\x01')
        prefix_manager.Add(16909060, '\x05')
        result = prefix_manager.Check(16909060)
        self.assertEqual(result, 32)


if __name__ == "__main__":
    unittest.main()