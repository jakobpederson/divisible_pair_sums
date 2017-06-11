from collections import namedtuple

Element = namedtuple('Element', ['index', 'value'])


class DivisiblePairSums():

    def __init__(self, n, k, ar):
        self.n = n
        self.k = k
        self.ar = ar
        self.ints = [Element(index=index, value=value) for index, value in enumerate(ar)]

    def answer_question(self):
        if self.validate_data():
            return len(
                [
                    (x.value, y.value) for x in self.ints
                    for y in self.ints if
                    (x.value + y.value) % self.k == 0 and
                    x.index < y.index]
            )
        return "Error: invalid input"

    def validate_data(self):
        if self.n > 100 or self.k > 100 or len(self.ar) > 100 or self.n < 2 or self.k < 1 or len(self.ar) < 1:
            return False
        return True
