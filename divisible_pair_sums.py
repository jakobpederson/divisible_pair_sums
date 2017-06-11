
class DivisiblePairSums():

    def __init__(self, n, k, ar):
        self.n = n
        self.k = k
        self.ints = ar
        self.list_of_tup = [(i, j) for i, j in enumerate(ar)]

    def answer_question(self):
        return len(
            [(x, y) for x in self.ints
             for y in self.ints if
             (x + y) % self.k == 0 and self.index_compare(x, y)])

    def index_compare(self, x, y):
        x_index = self.index_gen(x)
        y_index = self.index_gen(y)
        return list(x_index)[0] < list(y_index)[0]

    def index_gen(self, number):
        for value in self.list_of_tup:
            if value[1] == number:
                yield value[0]
