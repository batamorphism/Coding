# クラスカル
# C>0の時、連結であれば答えにcを加算し、unionしない
# C<0の時、必ずUnionする（罰金を払う必要はない)
import sys
sys.setrecursionlimit(10**6)


class UnionFind:
    def __init__(self, node_end):
        self.par = [i for i in range(node_end)]
        self.siz = [1] * node_end

    def find(self, x):
        if x == self.par[x]:
            return x
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
        self.siz[y] = 0

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    node_end, edge_end = map(int, input().split())
    edge_list = []
    for _ in range(edge_end):
        fr, to, co = map(int, input().split())
        fr -= 1
        to -= 1
        edge_list.append((fr, to, co))

    # コストが大きい順に見ていく
    edge_list.sort(key=lambda x: x[2])

    # クラスカル
    uf = UnionFind(node_end)
    ans = 0

    for fr, to, co in edge_list:
        if co <= 0:
            uf.union(fr, to)
        else:
            if uf.is_same(fr, to):
                ans += co
            else:
                uf.union(fr, to)

    print(ans)


main()
