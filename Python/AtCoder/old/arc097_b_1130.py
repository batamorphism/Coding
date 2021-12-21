import sys
sys.setrecursionlimit(10**6)
# (x, y) -> union(x, y)する
# iとp_iは、same(i, p_i)ならばいくつかの操作でi = p_iにできる


def main():
    n, m = map(int, input().split())
    P = [0] + list(map(int, input().split()))

    par = [i for i in range(n+1)]

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

    for _ in range(m):
        x, y = map(int, input().split())
        union(x, y)

    ans = 0
    for i, p in enumerate(P):
        if i == 0:
            continue
        if same(i, p):
            ans += 1
    print(ans)


main()
