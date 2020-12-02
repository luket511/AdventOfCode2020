import unittest

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

if __name__ == '__main__':
    unittest.main()