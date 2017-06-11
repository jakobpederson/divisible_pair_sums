import unittest
from divisible_pair_sums import DivisiblePairSums
from collections import namedtuple

Data = namedtuple('Data', ['n', 'k', 'ar'])

DATA1 = Data(n=6, k=3, ar=[1, 3, 2, 6, 1, 2])
DATA2 = Data(n=10, k=3, ar=[29, 97, 52, 86, 27, 89, 77, 19, 99, 96])
DATA3 = Data(n=100, k=22, ar=[
    43, 95, 51, 55, 40, 86, 65, 81, 51, 20, 47, 50, 65, 53, 23, 78,
    75, 75, 47, 73, 25, 27, 14, 8, 26, 58, 95, 28, 3, 23, 48, 69,
    26, 3, 73, 52, 34, 7, 40, 33, 56, 98, 71, 29, 70, 71, 28, 12,
    18, 49, 19, 25, 2, 18, 15, 41, 51, 42, 46, 19, 98, 56, 54, 98,
    72, 25, 16, 49, 34, 99, 48, 93, 64, 44, 50, 91, 44, 17, 63, 27,
    3, 65, 75, 19, 68, 30, 43, 37, 72, 54, 82, 92, 37, 52, 72, 62,
    3, 88, 82, 71
])


class DivsibilePairSumsTest(unittest.TestCase):

    def test_answer_question(self):
        first = DivisiblePairSums(DATA1.n, DATA1.k, DATA1.ar)
        second = DivisiblePairSums(DATA2.n, DATA2.k, DATA2.ar)
        third = DivisiblePairSums(DATA3.n, DATA3.k, DATA3.ar)
        self.assertEqual(5, first.answer_question())
        self.assertEqual(15, second.answer_question())
        self.assertEqual(216, third.answer_question())

    def test_validate_input(self):
        first = DivisiblePairSums(n=0, k=3, ar=[1, 2, 3])
        second = DivisiblePairSums(n=101, k=3, ar=[1, 2, 3])
        third = DivisiblePairSums(n=2, k=0, ar=[1, 2, 3])
        fourth = DivisiblePairSums(n=2, k=101, ar=[1, 2, 3])
        fifth = DivisiblePairSums(n=2, k=1, ar=[])
        sixth = DivisiblePairSums(n=2, k=1, ar=[x for x in range(0, 102)])
        self.assertEqual("Error: invalid input", first.answer_question())
        self.assertEqual("Error: invalid input", second.answer_question())
        self.assertEqual("Error: invalid input", third.answer_question())
        self.assertEqual("Error: invalid input", fourth.answer_question())
        self.assertEqual("Error: invalid input", fifth.answer_question())
        self.assertEqual("Error: invalid input", sixth.answer_question())
