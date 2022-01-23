import enum
import sys


# ダブリング
# 経路圧縮
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

    def dist(self, fr, to):
        # frからtoへの距離を求める
        lca_of_fr_to = self.lca(fr, to)
        return self.depth[fr] + self.depth[to] - 2 * self.depth[lca_of_fr_to]


def main():
    read = sys.stdin.buffer.read
    # Ctrl+Zで入力終了
    data = map(int, read().split())
    node_end = next(data)
    nei_of = [[] for _ in range(node_end)]
    for _ in range(node_end-1):
        a, b = next(data), next(data)
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)
    q_end = next(data)
    query_list = []
    for _ in range(q_end):
        k = next(data)
        query = []
        for _ in range(k):
            query.append(next(data)-1)
        query_list.append(query)

    lca = LCA(nei_of, 0)
    order = lca.order
    rev_order = [0] * lca.n
    for i, node in enumerate(order):
        rev_order[node] = i

    for query in query_list:
        # queryをdfsでの巡回順にソート
        query.sort(key=lambda x: rev_order[x])
        # queryの並び順で、経路を求めていく
        query_len = len(query)
        ans = 0
        for fr_i, fr in enumerate(query):
            to_i = (fr_i+1) % query_len
            to = query[to_i]
            ans += lca.dist(fr, to)
        print(ans//2)


main()
