def main():
    # input
    n = int(input())
    edge_list = []
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edge_list.append((w, u, v))

    edge_list.sort()

    # setup Union Find
    par = [i for i in range(n)]
    siz = [1]*n

    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        par[x] = y
        siz[y] += siz[x]

    def get_size(x):
        return siz[find(x)]

    ans = 0
    for w, fr, to in edge_list:
        # frとtoを結合
        # その時に、frのsubtreeとtoのsubtreeの間で、最短パスに含まれる辺の重みの最大値が設定される
        siz_fr = get_size(fr)
        siz_to = get_size(to)
        ans += w*siz_fr*siz_to
        union(fr, to)

    print(ans)


main()
