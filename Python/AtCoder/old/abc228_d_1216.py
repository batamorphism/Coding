import sys
sys.setrecursionlimit(10**6)
N = 2**20
NODE_END = 2**20+1
SUPER_NODE = NODE_END-1


def main():
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]

    A = [-1]*NODE_END

    # setup Union Find
    par = [i for i in range(NODE_END)]

    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]

    def union(x, y):
        # x < yとする
        if x > y:
            x, y = y, x
        x = find(x)
        y = find(y)
        if y == SUPER_NODE:
            y = 0
        par[x] = y

    def get_h(x):
        x %= N
        h = find(x)
        if h == SUPER_NODE:
            h = 0
        return h

    for query in query_list:
        t, x = query
        if t == 1:
            h = get_h(x)
            A[h] = x
            union(h, h+1)
        else:
            x %= N
            ans = A[x]
            print(ans)


main()
