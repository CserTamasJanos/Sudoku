import math


class ASudoku:
    def __init__(self, sor):
        self.beginning = []
        [self.beginning.append(number) for number in sor]
        self.Ssize = math.sqrt(len(sor))

    def DrawOut(self):
        i = 0
        while i < len(self.beginning):
            if self.beginning[i] == '0':
                print(".", end="")
            else:
                print(self.beginning[i], end="")
            if i % self.Ssize == self.Ssize - 1:
                print()
            i += 1