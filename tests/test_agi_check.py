import unittest
from arena import agi_check


class TestAgiCheck(unittest.TestCase):
    def test_agi_check(self):
        self.assertFalse(agi_check(8, 6))
        self.assertTrue(agi_check(6, 8))
        self.assertTrue(agi_check(8, 8))


if __name__ == "__main__":
    unittest.main()
