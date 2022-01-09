import sys
sys.setrecursionlimit(10**6)


def main():
    n = int(input())

    edge_list = []
    for _ in range(n-1):
        fr, to, we = map(int, input().split())
        fr -= 1
        to -= 1
        edge_list.append((fr, to, we))

    edge_list.sort(key=lambda x: x[2])

    # setup union find
    par = [i for i in range(n)]
    siz = [1 for _ in range(n)]

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

    def size(x):
        return siz[find(x)]

    ans = 0
    for fr, to, we in edge_list:
        if not same(fr, to):
            ans += size(fr)*size(to)*we
            union(fr, to)

    print(ans)


main()
