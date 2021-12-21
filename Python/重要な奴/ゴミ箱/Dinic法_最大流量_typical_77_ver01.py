# https://atcoder.jp/contests/typical90/submissions/25802721
import random

from collections import deque
import sys
sys.setrecursionlimit(10**5)


class Dinic:
    def __init__(self, n: int):
        """Dinic
        最大流を解くアルゴリズムO(N*N**0.5)

        Args:
            n (int): node数
        """
        self.n = n
        # 多分、from, cap, to, _
        # ここで、capは最大流量を流した後の、追加で流せる容量
        self.links = [[] for _ in range(n)]
        self.depth = None
        self.progress = None

    def add_link(self, _from: int, to: int, cap: int):
        """edgeを追加する

        Args:
            _from (int): edgeの始点を指すnode
            to (int): edgeの終点を指すnode
            cap (int): edgeの容量を指すnode
        """
        self.links[_from].append([cap, to, len(self.links[to])])
        self.links[to].append([0, _from, len(self.links[_from]) - 1])

    # sからの最短距離
    def bfs(self, s):
        depth = [-1] * self.n
        depth[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for cap, to, rev in self.links[v]:
                if cap > 0 and depth[to] < 0:
                    depth[to] = depth[v] + 1
                    q.append(to)
        self.depth = depth

    # 増加パスの探索
    def dfs(self, v, t, flow):
        if v == t:
            return flow
        links_v = self.links[v]
        for i in range(self.progress[v], len(links_v)):
            self.progress[v] = i
            cap, to, rev = link = links_v[i]
            if cap == 0 or self.depth[v] >= self.depth[to]:
                continue
            d = self.dfs(to, t, min(flow, cap))
            if d == 0:
                continue
            link[0] -= d
            self.links[to][rev][0] += d
            return d
        return 0

    def max_flow(self, s: int, t: int) -> int:
        """最大流量を計算する

        Args:
            s (int): 始点を指すnode
            t (int): 終点を指すnode

        Returns:
            int: 最大流量
        """

        flow = 0
        while True:
            self.bfs(s)
            if self.depth[t] < 0:
                return flow
            self.progress = [0] * self.n
            current_flow = self.dfs(s, t, float('inf'))
            while current_flow > 0:
                flow += current_flow
                current_flow = self.dfs(s, t, float('inf'))


def main():
    n, t = map(int, input().split())
    A = [list(map(int, input().split())) + [i] for i in range(n)]
    B = [list(map(int, input().split())) + [n+i] for i in range(n)]
    A.sort()  # なあにこれえ
    dic = {}  # dic[bxby] = i+n(各Bを指し示すnode)
    # 最大流の問題を解くDinic法を用いる
    G = Dinic(2*n+2)
    s = 2*n  # start
    g = 2*n+1  # goal
    times = 10**10  # bxbyをdicに登録できるようにする
    for bx, by, b_node in B:
        dic[bx*times+by] = b_node
        G.add_link(b_node, g, 1)  # 各Bからgへの容量1のedgeを張る

    for ax, ay, a_node in A:
        G.add_link(s, a_node, 1)  # sから各Aへの容量1のedgeを張る
        for di in [-t, 0, t]:
            for dj in [-t, 0, t]:
                # Aからの移動距離8パターンに対して処理
                if di == dj == 0:
                    continue
                moved_a = (ax+di)*times + ay+dj
                if moved_a in dic:
                    b_node = dic[moved_a]
                    G.add_link(a_node, b_node, 1)

    # 最大流量を計算する
    flow = G.max_flow(s, g)
    if flow != n:
        print("No")
        exit()

    print("Yes")

    def direction(ax, ay, bx, by):
        if ax + t == bx and ay + 0 == by: return 1
        if ax + t == bx and ay + t == by: return 2
        if ax + 0 == bx and ay + t == by: return 3
        if ax - t == bx and ay + t == by: return 4
        if ax - t == bx and ay + 0 == by: return 5
        if ax - t == bx and ay - t == by: return 6
        if ax + 0 == bx and ay - t == by: return 7
        if ax + t == bx and ay - t == by: return 8

    ans = [-1] * n
    for ax, ay, i in A:
        for cap, to, _ in G.links[i]:
            if cap == 0:  # and to < 2*n:
                bx, by, _ = B[to-n]
                ans[i] = direction(ax, ay, bx, by)
                break

    print(*ans)


main()
