# ワーシャルフロイド
# 二分探索
INF = float('inf')


def main():
    node_end, price_max, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(node_end)]

    X_list = []
    for r in range(node_end):
        for c in range(node_end):
            if A[r][c] == -1:
                X_list.append((r, c))

    # wf >= kとなる最大のxをx_hiとする
    # wf >= k+1となる最大のxをx_loとする
    # この差が答え
    def bisect(k):
        ok = 0
        ng = 10**11
        while ng - ok > 1:
            mid = (ok + ng) // 2
            set_X(A, X_list, mid)
            cnt = wf(A, price_max)
            if cnt >= k:
                ok = mid
            else:
                ng = mid
        return ok

    x_lo = bisect(k+1)
    x_hi = bisect(k)
    ans = x_hi - x_lo
    if ans > 10**9:
        ans = 'Infinity'
    print(ans)


def wf(A, p):
    # 隣接行列Aに対し
    # コストp以下で移動できる都市の組み合わせがいくつあるかを返す
    if p == 0:
        return INF

    n = len(A)
    DP = [[INF]*n for _ in range(n)]
    for k in range(n):
        for fr in range(n):
            for to in range(n):
                dp1 = A[fr][to]
                dp2 = DP[fr][k] + DP[k][to]
                dp3 = DP[fr][to]
                DP[fr][to] = min(dp1, dp2, dp3)

    ret = 0
    for fr in range(n):
        for to in range(fr+1, n):
            if DP[fr][to] <= p:
                ret += 1
    return ret


def set_X(A, X_list, x):
    # X_listに設定されたr, cに対し、xを設定する
    for r, c in X_list:
        A[r][c] = x


main()
