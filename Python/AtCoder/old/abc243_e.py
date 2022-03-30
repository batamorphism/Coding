import heapq
import sys
sys.setrecursionlimit(10**7)


class UnionFind:
    """
    UnionFind
    同じグループに入るかの判定、およびグループがいくつあるかの判定
    各グループはグラフ（木）で表現する
    AとBとをまとめる=AとBの間に辺を張る
    同じグループに入るかの判定は、要素をさかのぼって根が同じかを見ればよい
    """

    def __init__(self, n):
        """
        n: 頂点数
        """
        self._node_end = n
        self._par = [i for i in range(n)]
        self._siz = [1 for i in range(n)]

    def find(self, x):
        """
        xの代表元を返す
        """
        if self._par[x] == x:
            return x
        self._par[x] = self.find(self._par[x])
        return self._par[x]

    def union(self, x, y):
        """
        xとyとを同じグループとしてみなす
        """
        # self._add_tree(x)
        # self._add_tree(y)
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        # siz[x] <= siz[y]にする
        if self._siz[x] > self._siz[y]:
            x, y = y, x

        # サイズが大きいほうが親
        self._par[x] = y
        self._siz[y] += self._siz[x]

    def same(self, x, y):
        """
        xとyが同じグループかを比較する
        """
        return self.find(x) == self.find(y)

    # 以降、おまけ機能
    def members(self, x):
        """
        xと同じグループに属するメンバーをすべてリストで列挙する
        遅い
        """
        x = self.find(x)
        ret = []
        for node in range(self._node_end):
            if self.find(node) == x:
                ret.append(node)
        return ret

    def roots(self):
        """
        全ての連結成分の代表元をリストで返す
        遅い
        """
        ret = set()
        for node in range(self._node_end):
            root = self.find(node)
            ret.add(root)
        return list(ret)

    def count_groups(self):
        """
        グラフの連結成分の個数を返す
        遅い
        """
        return len(self.roots())

    def size(self, x):
        """
        xが属するグループの要素の数を返す
        """
        x = self.find(x)
        return self._siz[x]


INF = float('inf')
# O(N**3)までOK
# 全点間距離+クラスカル
# 足そうとしている辺が、元の全点間距離と同じであり、まだ連結でない場合はその辺を採用
def main():
    node_end, edge_end = map(int, input().split())
    edge_list = []
    for _ in range(edge_end):
        fr, to, cost = map(int, input().split())
        fr -= 1
        to -= 1
        edge_list.append((fr, to, cost))

    # 全点間距離
    dist = [[INF]*node_end for _ in range(node_end)]
    used_edge_of = [[[] for _ in range(node_end)] for _ in range(node_end)]
    for node in range(node_end):
        dist[node][node] = 0
    for i, (fr, to, cost) in enumerate(edge_list):
        dist[fr][to] = min(cost, dist[fr][to])
        dist[to][fr] = min(cost, dist[to][fr])
        used_edge_of[fr][to].append(i)
        used_edge_of[to][fr].append(i)
    for k in range(node_end):
        for fr in range(node_end):
            for to in range(node_end):
                dp1 = dist[fr][k] + dist[k][to]  # 今までの経路にkを追加
                # used[fr][k] + used[k][to]に含まれる辺が追加される
                dp2 = dist[fr][to]  # 今までの経路にkを追加しない
                used_edge_fr = used_edge_of[fr][k]
                used_edge_to = used_edge_of[k][to]
                used_edge_2 = used_edge_of[fr][to]
                if dp1 < dp2 or (dp1 == dp2 and len(used_edge_fr) + len(used_edge_to) < len(used_edge_2)):
                    used_edge_fr = used_edge_of[fr][k]
                    used_edge_to = used_edge_of[k][to]
                    if len(used_edge_fr) <= len(used_edge_to):
                        used_edge_to, used_edge_fr = used_edge_fr, used_edge_to
                    for edge in used_edge_to:
                        used_edge_fr.append(edge)
                    used_edge_of[fr][to] = used_edge_fr[:]
                    used_edge_of[to][fr] = used_edge_fr[:]
                dist[fr][to] = min(dp2, dp1)
                dist[to][fr] = min(dp2, dp1)

    used_edge_set = set()
    for fr in range(node_end):
        for to in range(node_end):
            used_edge = used_edge_of[fr][to]
            for edge in used_edge:
                used_edge_set.add(edge)
    cnt = len(used_edge_set)

    ans = edge_end - cnt
    print(ans)


def dkj(fr, to, nei_of, node_end):
    # ダイクストラ
    dist = [INF]*node_end
    dist[fr] = 0
    que = [(0, fr)]
    while que:
        pre_d, pre_node = heapq.heappop(que)
        if pre_d > dist[pre_node]:
            continue
        for cur_node, cur_cost in nei_of[pre_node]:
            cur_d = dist[pre_node] + cur_cost
            if dist[cur_node] <= cur_d:
                continue
            dist[cur_node] = cur_d
            heapq.heappush(que, (cur_d, cur_node))

    return dist[to]


main()
