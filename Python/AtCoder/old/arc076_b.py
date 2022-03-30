import sys
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.siz = [1 for i in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if not self.siz[x] <= self.siz[y]:
            x, y = y, x
        self.par[x] = y
        self.siz[y] += self.siz[x]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    node_end = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(node_end)]

    # nei_of[node] = [(nex_node, dist), ...]
    edge_list = []
    x_list = []
    y_list = []
    for i, (x, y) in enumerate(xy_list):
        x_list.append((x, i))
        y_list.append((y, i))

    x_list.sort()
    y_list.sort()

    for x_or_y_list in [x_list, y_list]:
        pre_x = x_or_y_list[0][0]
        pre_node = x_or_y_list[0][1]
        for x, node in x_or_y_list[1:]:
            d = abs(x-pre_x)
            edge_list.append((pre_node, node, d))
            pre_x = x
            pre_node = node

    # 最小全域木
    edge_list.sort(key=lambda x: x[2])
    uf = UnionFind(node_end)
    total_cost = 0
    for a, b, cost in edge_list:
        if not uf.is_same(a, b):
            uf.union(a, b)
            total_cost += cost

    # 与件から、必ず全域木になる
    print(total_cost)


main()
