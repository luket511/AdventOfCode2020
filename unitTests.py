import unittest
from commonFunctions import reader

# py unitTests.py -v

class AdventOfCodeUnitTests(unittest.TestCase):

    def test_day_one(self):
        import Input1test

        from Day_1a import bruteForcePairs, findMatchingPairs
        self.assertEqual(findMatchingPairs(2020,Input1test.LIST), [1721,299])
        self.assertEqual(bruteForcePairs(2020,Input1test.LIST), [1721,299])

        from Day_1b import bruteForceTrips, findMatchingTrips
        self.assertEqual(bruteForceTrips(2020,Input1test.LIST).sort(), [979, 366, 675].sort())
        self.assertEqual(findMatchingTrips(2020,Input1test.LIST).sort(), [979, 366, 675].sort())

    def test_day_two(self):
        from Day_2a import checkPasswords
        self.assertEqual(checkPasswords("Input2test.csv"),2)
        
        from Day_2b import checkPasswords
        self.assertEqual(checkPasswords("Input2test.csv"),1)

    def test_day_eleven(self):
        from Day_11a import Layout
        l1 = Layout(reader("input11test.csv"))
        self.assertEqual(l1.getFinalNumberOccupied(), 37)

        from Day_11b import AdvancedLayout
        l2 = AdvancedLayout(reader("input11test.csv"))
        self.assertEqual(l2.getFinalNumberOccupied(),26)

    def test_day_twelve(self):
        from Day_12a import Ship
        s1 = Ship()
        s1.navigate(reader("input12test.csv"))
        self.assertEqual(s1.getManhattenDistance(),25)

        from Day_12b import BetterShip
        s2 = BetterShip()
        s2.navigate(reader("input12test.csv"))
        self.assertEqual(s2.getManhattenDistance(),286)

if __name__ == '__main__':
    unittest.main()