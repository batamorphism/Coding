import sys
from collections import deque
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
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


# 強連結成分分解
# 強連結成分が2以上あるようなnodeへ到達しうる者が答え
def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    rev_nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to = map(int, input().split())
        fr -= 1
        to -= 1
        nei_of[fr].append(to)
        rev_nei_of[to].append(fr)

    # 戻り掛けにスタックに登録
    uf = UnionFind(node_end)
    stk = []

    first_step(stk, node_end, nei_of)
    second_step(stk, rev_nei_of, uf)

    # ufに強連結成分が設定されている
    is_cycle = [False]*node_end
    for node in range(node_end):
        if uf.size(node) >= 2:
            is_cycle[node] = True

    # is_cycleから逆向きに進めて、経路があればそれは答え
    INF = float('inf')
    dist = [INF]*node_end
    que = deque()
    for node in range(node_end):
        if is_cycle[node]:
            que.append(node)
            dist[node] = 0
    while que:
        pre = que.popleft()
        pre_d = dist[pre]
        cur_d = pre_d + 1
        for cur in rev_nei_of[pre]:
            if dist[cur] <= pre_d:
                continue
            dist[cur] = cur_d
            que.append(cur)

    ans = 0
    for node in range(node_end):
        if dist[node] != INF:
            ans += 1
    print(ans)


def second_step(stk, rev_nei_of, uf):
    done = [False]*len(stk)

    def dfs(node):
        # 非再帰でok
        cnt = 0
        que = [node]
        while que:
            pre = que.pop()
            if done[pre]:
                continue
            done[pre] = True
            for cur in rev_nei_of[pre]:
                if done[cur]:
                    continue
                que.append(cur)
                uf.union(pre, cur)
            cnt += 1
        return cnt

    # 逆向きにdfs
    while stk:
        node = stk.pop()
        if done[node]:
            continue
        dfs(node)


def first_step(stk, node_end, nei_of):
    done = [False]*node_end

    # 戻り掛けにスタックに登録
    def dfs(pre):
        done[pre] = True
        for cur in nei_of[pre]:
            if done[cur]:
                continue
            dfs(cur)
        stk.append(pre)

    for node in range(node_end):
        if done[node]:
            continue
        dfs(node)


main()
