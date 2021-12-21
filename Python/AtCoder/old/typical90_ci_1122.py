# Xが大きいほど、行ける町の数は少なくなる
# 行ける町の数がk個となる最大のXと、最小のXを求める
# 全点間最小距離はワーシャルフロイド
INF = 10**12


def main():
    n, p, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]

    X_list = []
    for r in range(n):
        for c in range(n):
            if A[r][c] == -1:
                X_list.append((r, c))

    def check(x):
        for r, c in X_list:
            A[r][c] = x
        # このAに対し、ワーシャルフロイド法を行う
        DP = [[INF]*n for _ in range(n)]
        for kk in range(n):
            for fr in range(n):
                for to in range(n):
                    dp1 = A[fr][to]
                    dp2 = DP[fr][kk] + DP[kk][to]
                    dp3 = DP[fr][to]
                    DP[fr][to] = min(dp1, dp2, dp3)
        # 距離がp以下となる組み合わせを求める
        cnt = 0
        for fr in range(n):
            for to in range(fr+1, n):
                if DP[fr][to] <= p:
                    cnt += 1
        return cnt

    # 行ける町の数がk以下となる最小のxを求める
    ok = INF
    ng = 0
    while ok-ng > 1:
        mid = (ok+ng) // 2
        cnt = check(mid)
        if cnt <= k:
            ok = mid
        else:
            ng = mid
    lo = ok

    # 行ける町の数がk-1以下となる最小のxを求める
    ok = INF
    ng = 0
    while ok-ng > 1:
        mid = (ok+ng) // 2
        cnt = check(mid)
        if cnt <= k-1:
            ok = mid
        else:
            ng = mid
    hi = ok

    ans = hi-lo
    if ans < 0:
        ans = 0
    if ans > INF//2:
        print('Infinity')
        return
    print(ans)


main()
