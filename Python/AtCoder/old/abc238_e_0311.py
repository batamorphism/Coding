import sys
sys.setrecursionlimit(10**6)


def main():
    n, q = map(int, input().split())

    # setup union find
    par = [i for i in range(n+10)]
    siz = [1]*(n+10)

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
        # siz[x] < siz[y]
        if not (siz[x] <= siz[y]):
            x, y = y, x
        par[x] = y
        siz[y] += siz[x]
        siz[x] = 0

    def is_same(x, y):
        return find(x) == find(y)

    edge_list = [tuple(map(int, input().split())) for _ in range(q)]
    for le, ri in edge_list:
        le -= 1
        if is_same(le, ri):
            continue
        union(le, ri)

    is_yes = is_same(0, n)

    if is_yes:
        print('Yes')
    else:
        print('No')


main()
