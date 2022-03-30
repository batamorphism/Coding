# [le, ri+1)の和が分かる
# leとri+1をつないで、0とnが連結になればおｋ
def main():
    n, q = map(int, input().split())
    n += 1
    edge_list = []
    for _ in range(q):
        le, ri = map(int, input().split())
        le -= 1
        edge_list.append((le, ri))

    # setup union find
    par = [i for i in range(n)]
    siz = [1]*n

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
        if siz[x] < siz[y]:
            x, y = y, x
        par[y] = x
        siz[x] += siz[y]
        siz[y] = 0

    def is_same(x, y):
        return find(x) == find(y)

    for le, ri in edge_list:
        union(le, ri)

    if is_same(0, n-1):
        print('Yes')
    else:
        print('No')


main()
