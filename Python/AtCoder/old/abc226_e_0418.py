import sys
sys.setrecursionlimit(10 ** 6)
MOD = 998244353
# なもりグラフ
# 円環の個数cntにつき、答えは2**cnt個


class UnionFind:
    def __init__(self, node_end):
        self.node_end = node_end
        self.par = [i for i in range(node_end)]
        self.siz = [1] * node_end
        self.edge_cnt = [0] * node_end

    def find(self, x):
        if x == self.par[x]:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            self.edge_cnt[x] += 1
            return
        if self.siz[x] < self.siz[y]:
            x, y = y, x
        self.par[y] = x
        self.siz[x] += self.siz[y]
        self.edge_cnt[x] += self.edge_cnt[y] + 1
        self.siz[y] = 0

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.siz[self.find(x)]

    def get_edge_cnt(self, x):
        return self.edge_cnt[self.find(x)]


def main():
    node_end, edge_end = map(int, input().split())
    edge_list = []
    for _ in range(edge_end):
        fr, to = map(int, input().split())
        fr -= 1
        to -= 1
        edge_list.append((fr, to))

    uf = UnionFind(node_end)
    for fr, to in edge_list:
        uf.union(fr, to)

    namori_set = set()
    for i in range(node_end):
        root = uf.find(i)
        node_cnt = uf.get_size(root)
        edge_cnt = uf.get_edge_cnt(root)
        if node_cnt == edge_cnt:
            namori_set.add(root)
        else:
            print(0)
            return
    cnt = len(namori_set)
    print(pow(2, cnt, MOD))


main()
