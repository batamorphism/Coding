import sys
sys.setrecursionlimit(10**6)
# x軸y軸独立に考えと
# x軸が近いものかy軸が近いもの同士をくっつけるのが最適


def main():
    n = int(input())
    X = []
    Y = []
    for i in range(n):
        x, y = map(int, input().split())
        X.append((x, i))
        Y.append((y, i))

    X.sort()
    Y.sort()
    edge_list = []
    for i in range(n-1):
        cost = X[i+1][0]-X[i][0]
        x1, x2 = X[i][1], X[i+1][1]
        edge_list.append((cost, x1, x2))

    for i in range(n-1):
        cost = Y[i+1][0]-Y[i][0]
        x1, x2 = Y[i][1], Y[i+1][1]
        edge_list.append((cost, x1, x2))
    del X, Y

    edge_list.sort()

    # クラスカル
    # setup union find
    par = [i for i in range(n)]

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

    def same(x, y):
        return find(x) == find(y)

    ans = 0
    for cost, x1, x2 in edge_list:
        if not same(x1, x2):
            ans += cost
            union(x1, x2)

    print(ans)


main()
