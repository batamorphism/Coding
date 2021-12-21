import sys
sys.setrecursionlimit(10**6)


def main():
    n = int(input())
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]

    par = [i for i in range(n + 1)]
    A = [0]*(n + 1)

    # クエリ先読み
    for t, x, y, v in sorted(query_list):
        if t == 1:
            continue
        # A[x]+A[y]=vより
        A[y] = v - A[x]

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

    for t, x, y, v in query_list:
        if t == 0:
            union(x, y)
        else:
            if not same(x, y):
                print('Ambiguous')
                continue

            # A[x] = vと仮定した時の、A[y]を求める
            d = v-A[x]
            if (y-x) % 2 == 0:
                # xとyが偶数個離れているとき、動き方は同じになる
                ans = A[y] + d
            else:
                ans = A[y] - d
            print(ans)


main()
