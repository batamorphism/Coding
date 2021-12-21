# https://gitlab.com/w0mbat/kyopro_educational_90/-/blob/main/077.py
from typing import List, Tuple


class BipartiteMatching:
    '''二部マッチング問題のソルバー。
    https://snuke.hatenablog.com/entry/2019/05/07/013609 のコードをPythonにベタ移植したもの。
    snuke is God.
    '''

    def __init__(self, n: int, m: int) -> None:
        """二部マッチング問題のソルバー
        n対mの組に対してマッチングを行う?
        Args:
            n (int): 頂点数
            m (int): ???多分毎回nと同じでよい?
        """
        self._n = n
        self._m = m
        self._to: List[List[int]] = [[] for _ in range(n)]

    def add_edge(self, a: int, b: int) -> None:
        self._to[a].append(b)

    def solve(self) -> List[Tuple[int, int]]:
        """回答する

        Returns:
            List[Tuple[int, int]]: 二部マッチングした際の頂点の組み合わせ
        """
        n, m, to = self._n, self._m, self._to
        pre = [-1] * n
        root = [-1] * n
        p = [-1] * n
        q = [-1] * m
        upd = True
        while upd:
            upd = False
            s = []
            s_front = 0
            for i in range(n):
                if p[i] == -1:
                    root[i] = i
                    s.append(i)
            while s_front < len(s):
                v = s[s_front]
                s_front += 1
                if p[root[v]] != -1:
                    continue
                for u in to[v]:
                    if q[u] == -1:
                        while u != -1:
                            q[u] = v
                            p[v], u = u, p[v]
                            v = pre[v]
                        upd = True
                        break
                    u = q[u]
                    if pre[u] != -1:
                        continue
                    pre[u] = v
                    root[u] = root[v]
                    s.append(u)
            if upd:
                for i in range(n):
                    pre[i] = -1
                    root[i] = -1
        return [(v, p[v]) for v in range(n) if p[v] != -1]


import sys

input = lambda: sys.stdin.readline().strip()

n, t = map(int, input().split())
a = sorted([tuple(list(map(int, input().split()))+[i]) for i in range(n)])
b = sorted([tuple(map(int, input().split())) for _ in range(n)])
d = {}
for i in range(n):
    d[b[i]] = i
G = BipartiteMatching(n, n)
for i in range(n):
    for j in [-t, 0, t]:
        for k in [-t, 0, t]:
            if (j != 0 or k != 0) and (a[i][0] + j, a[i][1] + k) in d:
                G.add_edge(i, d[(a[i][0]+j, a[i][1]+k)])
m = G.solve()
if len(m) == n:
    print('Yes')
    ans = [0] * n
    for e in m:
        ax = a[e[0]][0]
        ay = a[e[0]][1]
        bx = b[e[1]-n][0]
        by = b[e[1]-n][1]
        if bx == ax + t and by == ay:
            ans[a[e[0]][2]] = 1
        elif bx  == ax + t and by == ay + t:
            ans[a[e[0]][2]] = 2
        elif bx == ax and by == ay + t:
            ans[a[e[0]][2]] = 3
        elif bx == ax - t and by == ay + t:
            ans[a[e[0]][2]] = 4
        elif bx == ax - t and by == ay:
            ans[a[e[0]][2]] = 5
        elif bx == ax - t and by == ay - t:
            ans[a[e[0]][2]] = 6
        elif bx == ax and by == ay - t:
            ans[a[e[0]][2]] = 7
        else:
            ans[a[e[0]][2]] = 8
    print(*ans)
else:
    print('No')
