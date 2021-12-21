from collections import deque
import sys
sys.setrecursionlimit(10**6)


def main():
    node_end, edge_end = map(int, input().split())
    cannot_move_pair = node_end*(node_end-1)//2

    query_list = []
    for _ in range(edge_end):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        query_list.append((a, b))

    # 橋をつないでいくことを考える
    # 橋をつなぐと、もともとお互いが連結でない場合に
    # その左右の集合の大きさをsiz_le, siz_riとして、
    # siz_le*siz_riだけ不便さが減少する

    # setup union find
    par = [i for i in range(node_end)]
    siz = [1 for _ in range(node_end)]

    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        par[x] = y
        siz[y] += siz[x]

    def same(x, y):
        return find(x) == find(y)

    def get_siz(x):
        x = find(x)
        return siz[x]

    ans_list = deque()

    for a, b in query_list[::-1]:
        ans_list.appendleft(cannot_move_pair)
        if not same(a, b):
            # 橋をつなぐ
            cannot_move_pair -= get_siz(a)*get_siz(b)
            union(a, b)

    for ans in ans_list:
        print(ans)


main()
