# doubling
class LCA():
    def __init__(self, links, root):
        self.n = len(links)
        self.dbl = [[-1] for _ in range(self.n)]
        self.depth = [-1] * self.n
        self.depth[root] = 0
        # DFSでの巡回順 order[i]でi番目に通った頂点
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
    edge_list = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        edge_list[a-1].append(b-1)
        edge_list[b-1].append(a-1)
    lca = LCA(links=edge_list, root=0)

    q = int(input())
    k_list = []
    query = []
    for _ in range(q):
        k, *v = list(map(int, input().split()))
        v = [vv-1 for vv in v]
        k_list.append(k)
        query.append(v)

    # order_list[node]でnodeが何番目に通ったか
    order_list = [0]*n
    for i, v in enumerate(lca.order):
        order_list[v] = i

    for v_list in query:
        # v_listの要素をlca.orderの順でsort
        v_list_order = [(order_list[v], v) for v in v_list]
        v_list_order.sort()
        ans = 0
        for i in range(len(v_list)):
            # 各頂点vの最短距離の総和
            _, v0 = v_list_order[i-1]
            _, v1 = v_list_order[i]
            d = lca.depth[v0]+lca.depth[v1]-lca.depth[lca.lca(v0, v1)]*2
            ans += d
        print(ans//2)


main()
