# 最初にC>0は全てUnionFindしておき
# 罰金が付くやつはとりあえず残しておいて
# 賞金が付くやつを削る
import sys
sys.setrecursionlimit(10 ** 7)


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edge_list = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edge_list.append((c, a, b))
    edge_list.sort()

    # setup union find
    par = [i for i in range(n)]

    def find(x):
        if par[x] == x:
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

    ans = 0
    for cost, fr, to in edge_list:
        if cost < 0:
            union(fr, to)
        else:
            if not same(fr, to):
                union(fr, to)
            else:
                ans += cost
    print(ans)


main()
