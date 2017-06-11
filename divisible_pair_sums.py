
class DivisiblePairSums():

    def __init__(self, n, k, ar):
        self.n = n
        self.k = k
        self.ints = ar

    def answer_question(self):
        return len(
            [(x, y) for x in self.ints for y in self.ints if (x + y) % self.k == 0 and x < y]
        )
