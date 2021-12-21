import sys
sys.setrecursionlimit(10**6)


def main():
    n, q = map(int, input().split())
    nei_of = [[] for _ in range(n)]
    query_list = []

    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    for _ in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        query_list.append((c, d))

    # ci -> diの距離が奇数ならば道路で出会うし、偶数ならば町上で出会う
    # 0からの距離をすべて記憶しておく
    # d(ci, di) = d(0, ci)+d(0, di)-d(0, lca(ci, di))*2
    # したがって、mod 2上では
    # d(ci, di) = d(0, ci)+d(0, di)
    # よって、0からの距離をD[node]として記憶しておけばよい
    D = [-1]*n

    def dist(fr, to):
        return D[fr]+D[to]

    # Setup D
    def dfs(pre):
        for cur in nei_of[pre]:
            if D[cur] == -1:
                D[cur] = D[pre]+1
                dfs(cur)

    D[0] = 0
    dfs(0)
    # print(D)

    # Query
    for fr, to in query_list:
        d = dist(fr, to)
        if d % 2 == 1:
            print('Road')
        else:
            print('Town')
    return


main()
