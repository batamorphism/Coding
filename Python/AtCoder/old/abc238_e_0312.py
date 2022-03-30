import sys
sys.setrecursionlimit(10**6)


class UnionFnd:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.siz = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.siz[x] < self.siz[y]:
            x, y = y, x
        self.par[y] = x
        self.siz[x] += self.siz[y]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    n, q = map(int, input().split())
    uf = UnionFnd(n+10)
    for _ in range(q):
        le, ri = map(int, input().split())
        # (le, ri]で考える
        le -= 1
        uf.union(le, ri)

    if uf.is_same(0, n):
        print('Yes')
    else:
        print('No')


main()
