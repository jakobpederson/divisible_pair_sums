from collections import namedtuple

Element = namedtuple('Element', ['index', 'value'])


class DivisiblePairSums():

    def __init__(self, n, k, ar):
        self.n = n
        self.k = k
        self.ints = [Element(index=count, value=value) for count, value in enumerate(ar)]

    def answer_question(self):
        return len(
            [
                (x.value, y.value) for x in self.ints
                for y in self.ints if
                (x.value + y.value) % self.k == 0 and
                x.index < y.index
            ]
        )

