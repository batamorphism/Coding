import sys
sys.setrecursionlimit(10**9)


def main():
    n = int(input())
    par = [i for i in range(n)]
    siz = [1]*n

    # UNION FIND
    def union(x, y):
        x = find(x)
        y = find(y)
        siz[y] += siz[x]
        par[x] = y

    def find(x):
        if par[x] == x:
            return x
        par[x] = find(par[x])
        return par[x]

    def getsize(x):
        return siz[find(x)]

    edge_list = []
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edge_list.append((w, u, v))
    edge_list.sort()
    ans = 0
    for edge in edge_list:
        w, x, y = edge
        cnt = getsize(x)*getsize(y)
        union(x, y)
        ans += cnt*w
    print(ans)


main()
