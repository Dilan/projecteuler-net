import unittest
p54 = __import__("problem-054")

class Problem_054_Test(unittest.TestCase):

    def test_high_card(self):
        hand = p54.build_hand('2C 4D 6C TD TS')

        self.assertEqual(hand.statistics['one_pair'] is not None, True)
        self.assertEqual(hand.best(), 20010060402)

if __name__ == '__main__':
    unittest.main()