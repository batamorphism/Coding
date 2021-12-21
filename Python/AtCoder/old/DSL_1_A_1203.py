import sys
sys.setrecursionlimit(10**6)


def main():
    n, q = map(int, input().split())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]

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

    for com, x, y in query_list:
        if com == 0:
            union(x, y)
        else:
            if same(x, y):
                print(1)
            else:
                print(0)


main()
