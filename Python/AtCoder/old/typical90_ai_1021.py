import sys
read = sys.stdin.buffer.read


# doubling
class LCA():
    def __init__(self, links, root):
        """LCAを計算する木の構造

        Args:
            links (list): 隣接リスト
            root (int): 頂点
        """
        self.n = len(links)
        self.dbl = [[-1] for _ in range(self.n)]
        self.depth = [-1] * self.n
        self.depth[root] = 0
        # DFSでの巡回順
        self.order = []
        stack = [root]
        while stack:
            i = stack.pop()
            self.order.append(i)
            for j in links[i]:
                if self.depth[j] != -1:
                    continue
                self.depth[j] = self.depth[i] + 1
                self.dbl[j][0] = i
                stack.append(j)

        self.log_d = (max(self.depth)).bit_length()
        for j in range(self.log_d - 1):
            for i in range(self.n):
                ancestor = self.dbl[i][j]
                self.dbl[i].append(self.dbl[ancestor][j])

    def lca(self, x, y):
        # xとyのlcaを求める
        assert (self.depth[x] >= 0) and (self.depth[y] >= 0)
        if(self.depth[x] < self.depth[y]):
            x, y = y, x
        dif = self.depth[x] - self.depth[y]
        for bi in range(self.log_d):
            if(dif >> bi) & 1:
                x = self.dbl[x][bi]

        if(x == y):
            return x
        for bi in range(self.log_d-1, -1, -1):
            if(self.dbl[x][bi] != self.dbl[y][bi]):
                x = self.dbl[x][bi]
                y = self.dbl[y][bi]
        return self.dbl[x][0]


def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    lca = LCA(nei_of, 0)

    # 各クエリを、lca.orderの順番でソートしなおす
    order_dict = {node: i for i, node in enumerate(lca.order)}

    q = int(input())
    query_list = []
    for _ in range(q):
        _, *v = list(map(int, input().split()))
        v = [(order_dict[vv-1], vv-1) for vv in v]
        v.sort()
        v = [vv for _, vv in v]
        query_list.append(v)

    for query in query_list:
        ans = 0
        for i in range(len(query)):
            fr = query[i-1]
            to = query[i]
            lc = lca.lca(fr, to)
            dist = lca.depth[fr]+lca.depth[to]-lca.depth[lc]*2
            ans += dist
        print(ans//2)


main()
