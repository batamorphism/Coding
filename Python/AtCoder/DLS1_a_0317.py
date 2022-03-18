def main():
    node_end, query_end = map(int, input().split())

    # setup union find
    par = [i for i in range(node_end)]
    siz = [1] * node_end

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
        if siz[x] > siz[y]:
            x, y = y, x
        par[x] = y
        siz[y] += siz[x]
        siz[x] = 0

    def is_same(x, y):
        return find(x) == find(y)

    for _ in range(query_end):
        c, x, y = map(int, input().split())
        if c == 0:
            union(x, y)
        else:
            if is_same(x, y):
                print(1)
            else:
                print(0)


main()
