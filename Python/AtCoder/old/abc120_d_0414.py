import sys
sys.setrecursionlimit(10**6)


# 逆から考える
# 新たに通れるようになった組の数だけ、不便さが減る
class UnionFiond:
    def __init__(self, node_end):
        self.node_end = node_end
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

    def get_siz(self, x):
        return self.siz[self.find(x)]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    node_end, edge_end = map(int, input().split())
    edge_list = []
    for _ in range(edge_end):
        fr, to = map(int, input().split())
        fr -= 1
        to -= 1
        edge_list.append((fr, to))

    uf = UnionFiond(node_end)
    ans = node_end * (node_end-1) // 2
    ans_list = [ans]
    for fr, to in reversed(edge_list):
        if uf.is_same(fr, to):
            ans_list.append(ans)
        else:
            fr_siz = uf.get_siz(fr)
            to_siz = uf.get_siz(to)
            ans -= fr_siz * to_siz
            ans_list.append(ans)
            uf.union(fr, to)
    ans_list.pop()
    ans_list.reverse()
    print(*ans_list)


main()
