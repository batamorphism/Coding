import sys
sys.setrecursionlimit(10**6)


def main():
    n = int(input())
    n += 1
    q = int(input())
    query_list = []
    query0_list = []
    for _ in range(q):
        t, x, y, v = map(int, input().split())
        query_list.append((t, x, y, v))
        if t == 0:
            query0_list.append((x, y, v))

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

    # クエリ先読み
    query0_list.sort()
    A = [0] * (n+1)
    for x, y, v in query0_list:
        # x+y = v
        # y = v - x
        A[y] = v - A[x]

    for t, x, y, v in query_list:
        if t == 0:
            union(x, y)
        else:
            if not same(x, y):
                print('Ambiguous')
                continue

            delta = v - A[x]
            # A[x]をdeltaだけ加算すると
            # x+1は-delta, x+2は+delta, ...となる
            ans = A[y]
            if abs(y-x) % 2 == 0:
                ans += delta
            else:
                ans -= delta
            print(ans)


main()
