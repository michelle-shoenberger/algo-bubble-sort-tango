import unittest
from bubble_sort import bubble_sort

class BubbleTester(unittest.TestCase):

    test_numbers = [4, 3, 5, 0, 1]
    test_ans = [0, 1, 3, 4, 5]


    def test_return(self):
        """ This tests that function returns a value"""
        self.assertIsNotNone(bubble_sort([4, 3, 5, 0, 1]))

    def test_simple(self):
        ans = bubble_sort(self.test_numbers)
        self.assertListEqual(ans[0], self.test_ans)
        self.assertEqual(ans[1], 7)
        self.assertEqual(ans[2], 4)



if __name__ == "__main__":
    unittest.main()