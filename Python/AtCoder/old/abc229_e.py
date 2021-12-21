from collections import deque
import sys
sys.setrecursionlimit(10**6)
# 逆順に処理する
# Union Find
# 連結成分は、最初はn個ある
# a, bを連結すると、もともと連結だった場合は連結成分はかわらず
# 連結でなかった場合は、連結成分が-1


def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if a > b:
            a, b = b, a
        # a < bとする
        nei_of[a].append(b)

    # setup union find
    par = [i for i in range(node_end)]

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

    def same(x, y):
        return find(x) == find(y)

    # 逆順に処理する
    ans_que = deque()
    cnt = 0
    for del_node in range(node_end - 1, -1, -1):
        ans_que.appendleft(cnt)
        cnt += 1  # 頂点が出来上がることで、連結成分が増える
        for node in nei_of[del_node]:
            if not same(del_node, node):  # 関係するノードをつないでいく
                union(del_node, node)
                cnt -= 1

    for ans in ans_que:
        print(ans)


main()
