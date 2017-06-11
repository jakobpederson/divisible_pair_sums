import unittest
from divisible_pair_sums import DivisiblePairSums
from collections import namedtuple

Data = namedtuple('Data', ['n', 'k', 'ar'])

DATA1 = Data(n=6, k=3, ar=[1, 3, 2, 6, 1, 2])
DATA2 = Data(n=10, k=3, ar=[29, 97, 52, 86, 27, 89, 77, 19, 99, 96])


class DivsibilePairSumsTest(unittest.TestCase):

    def test_answer_question(self):
        first = DivisiblePairSums(DATA1.n, DATA1.k, DATA1.ar)
        second = DivisiblePairSums(DATA2.n, DATA2.k, DATA2.ar)
        self.assertEqual(5, first.answer_question())
        self.assertEqual(15, second.answer_question())
