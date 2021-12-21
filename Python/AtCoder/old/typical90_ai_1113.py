
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

    q_end = int(input())
    query_list = []
    for _ in range(q_end):
        _, *V = map(int, input().split())
        V = [v-1 for v in V]
        query_list.append(V)

    lca = LCA(nei_of, 0)
    ord_dict = {node: ord for ord, node in enumerate(lca.order)}
    # node -> dfsの探索順を返す関数

    def sort_key(node):
        return ord_dict[node]

    for query in query_list:
        # query上のnode間の距離を求める
        # queryを、lcaのdfs探索順にソートする
        query.sort(key=sort_key)
        query_ri = query[1:] + [query[0]]
        query_le = query
        dist_sum = 0
        for le, ri in zip(query_le, query_ri):
            dist = lca.depth[le] + lca.depth[ri] - 2*lca.depth[lca.lca(le, ri)]
            # print(le+1, ri+1, dist)
            dist_sum += dist
        print(dist_sum >> 1)


main()
