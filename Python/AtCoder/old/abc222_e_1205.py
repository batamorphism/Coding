import sys
sys.setrecursionlimit(10**6)
mod = 998244353


def main():
    # dfsをm回繰り返す
    # edgeに番号を付けて置き、目的地に着いたところから戻りがけに辺に1を追加していく
    n, m, k = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]

    nei_of = [[] for _ in range(n)]
    for i in range(n-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        nei_of[u].append((v, i))
        nei_of[v].append((u, i))

    # 各edgeを通った回数をセットする
    cnt = [0]*(n-1)
    for fr_i in range(len(A)-1):
        to_i = fr_i + 1
        fr, to = A[fr_i], A[to_i]
        set_cnt(cnt, fr, to, nei_of)

    # print(cnt)
    # 各cntに対し、+1, -1してkにする
    # sum(cnt)を足して
    # +2, +0してk+sum(cnt)にする
    # ナップザックDP
    val = k+sum(cnt)
    if val % 2 == 1:
        print(0)
        return

    if val < 0:
        print(0)
        return

    val //= 2
    item_list = [0] + cnt
    # itemからいくつか選んでvalにする組み合わせがいくつあるか
    # DP[i][v] = itemのうちi番目まで選んで、vになる組み合わせの個数
    # DP[i][v] = DP[i-1][v] + DP[i-1][v-item[i]]
    # DP[0][0] = 1, else 0
    DP = [[0]*(val+1) for _ in range(n)]
    DP[0][0] = 1
    for i in range(1, n):
        for v in range(val+1):
            DP[i][v] = DP[i-1][v]
            if v >= item_list[i]:
                DP[i][v] += DP[i-1][v-item_list[i]]
                DP[i][v] %= mod
    ans = DP[n-1][val]
    ans %= mod
    print(ans)


def set_cnt(cnt, fr, to, nei_of):
    n = len(nei_of)
    col = ['w']*n

    def dfs(pre):
        ret = 0
        if pre == to:
            return 1
        for cur, edge_id in nei_of[pre]:
            if col[cur] == 'w':
                col[cur] = 'g'
                val = dfs(cur)
                cnt[edge_id] += val
                ret = max(ret, val)
        return ret

    col[fr] = 'b'
    dfs(fr)


main()
