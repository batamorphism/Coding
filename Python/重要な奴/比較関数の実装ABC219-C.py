class Data():
    def __init__(self, x, val):
        self.x = x
        self.val = val

    def __lt__(self, other):
        # self.val < other.val
        lower = self.val
        greater = other.val
        L = min(len(lower), len(greater))
        for i in range(L):
            if not (lower[i] == greater[i]):
                j = i
                return self.check(lower[j], greater[j])
        return len(lower) < len(greater)

    def check(self, lower, greater):
        for xx in self.x:
            if lower == xx:
                return True
            if greater == xx:
                return False


def main():
    x = input()
    n = int(input())
    S_ = [input() for _ in range(n)]
    S = []
    for i in range(n):
        data = Data(x, S_[i])
        S.append(data)
    S = sorted(S)
    for i in range(n):
        print(S[i].val)


main()
