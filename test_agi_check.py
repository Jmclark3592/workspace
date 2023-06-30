import unittest

def agi_check(stat_c, stat_p):
    if stat_c > stat_p:
        return False
    else:
        return True

class TestAgiCheck(unittest.TestCase):
    def test_agi_check(self):
        self.assertFalse(agi_check(8, 6))
        self.assertTrue(agi_check(6, 8))
        self.assertTrue(agi_check(8, 8))

if __name__ == '__main__':
    unittest.main()