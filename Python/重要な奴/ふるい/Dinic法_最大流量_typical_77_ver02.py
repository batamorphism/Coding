# https://atcoder.jp/contests/typical90/submissions/25802721
# https://ikatakos.com/pot/programming_algorithm/graph_theory/maximum_flow

from collections import deque
import sys
sys.setrecursionlimit(10**5)


class Dinic:
    def __init__(self, n: int):
        """Dinic
        最大流を解くアルゴリズム

        Args:
            n (int): node数
        """
        self.n = n
        # 始点, 容量, 終点, 逆辺を指すindex
        # ここで、capは追加で流せる容量
        self.links = [[] for _ in range(n)]
        # sからの深さからなるリスト
        self.depth = [-1]*self.n
        # 各nodeについて、dfsでiterをいくつまで見たか
        self.progress = [0]*self.n
        self.INF = 10**10

    def add_link(self, b_node: int, e_node: int, cap: int):
        """edgeを追加する

        Args:
            b_node (int): edgeの始点を指すnode
            e_node (int): edgeの終点を指すnode
            cap (int): edgeの容量を指すnode
        """
        e_node_ind = len(self.links[e_node])  # links[e_node][e_node_ind]が逆辺
        b_node_ind = len(self.links[b_node])
        self.links[b_node].append([cap, e_node, e_node_ind])
        self.links[e_node].append([0, b_node, b_node_ind])

    # sからのdepthを幅優先探索で計算する
    # ただし、容量が正のedgeのみが対象
    def bfs(self, s_node):
        depth = [-1]*self.n
        depth[s_node] = 0
        que = deque([s_node])
        while que:
            pre_node = que.popleft()
            for cap, cur_node, rev in self.links[pre_node]:
                if cap > 0 and depth[cur_node] < 0:
                    depth[cur_node] = depth[pre_node] + 1
                    que.append(cur_node)
        self.depth = depth

    # depthが深くなる方向にのみたどって
    # フローを流し、capを減らす
    # 同時に、逆辺のcapは増やす(逆流ができる)
    # ここの再帰が深くなると遅い
    def dfs(self, s_node: int, g_node: int, flow):
        """flowを追加で流し流量を計算する
        ただし、bfsで計算したdepth順にのみ流す

        Args:
            s_node (int): flowを流す元のnode
            g_node (int): 終点を指すnode
            flow ([type]): s_nodeに流すflow

        Returns:
            [type]: g_nodeに流れたflow
        """
        if s_node == g_node:
            return flow
        links_of_s = self.links[s_node]
        for i in range(self.progress[s_node], len(links_of_s)):
            self.progress[s_node] = i
            link_of_s = links_of_s[i]
            cap, cur_node, rev = link_of_s
            if cap == 0 or self.depth[s_node] >= self.depth[cur_node]:
                continue
            add_flow = self.dfs(cur_node, g_node, min(flow, cap))
            if add_flow == 0:
                continue
            link_of_s[0] -= add_flow  # 追加で流した分capを減らす
            rev_link_of_s = self.links[cur_node][rev]
            rev_link_of_s[0] += add_flow
            return add_flow
        return 0

    def max_flow(self, s_node: int, g_node: int) -> int:
        """最大流量を計算する

        Args:
            s_node (int): 始点を指すnode
            g_node (int): 終点を指すnode

        Returns:
            int: 最大流量
        """

        flow = 0
        while True:
            self.bfs(s_node)
            if self.depth[g_node] < 0:
                # capに余裕があるedgeをたどってg_nodeまで行けないので停止
                return flow
            self.progress = [0]*self.n
            add_flow = self.dfs(s_node, g_node, self.INF)
            while add_flow > 0:  # 追加で流せる限り繰り返し、流せなくなったらdepth再計算
                flow += add_flow
                add_flow = self.dfs(s_node, g_node, self.INF)


def main():
    n, t = map(int, input().split())
    A = [list(map(int, input().split())) + [i] for i in range(n)]
    B = [list(map(int, input().split())) + [n+i] for i in range(n)]
    A.sort()  # なあにこれえ よくわからないけど、同じグループに入らなさそうなものから処理していくといいっぽい？
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
        if ax + t == bx and ay + 0 == by:
            return 1
        if ax + t == bx and ay + t == by:
            return 2
        if ax + 0 == bx and ay + t == by:
            return 3
        if ax - t == bx and ay + t == by:
            return 4
        if ax - t == bx and ay + 0 == by:
            return 5
        if ax - t == bx and ay - t == by:
            return 6
        if ax + 0 == bx and ay - t == by:
            return 7
        if ax + t == bx and ay - t == by:
            return 8

    ans = [-1] * n
    for ax, ay, i in A:
        for cap, to, _ in G.links[i]:
            if cap == 0:  # and to < 2*n:
                bx, by, _ = B[to-n]
                ans[i] = direction(ax, ay, bx, by)
                break

    print(*ans)


main()
