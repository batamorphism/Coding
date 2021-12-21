# ワーシャルフロイド法を、コストを変えながら行う
# Xを決め打ちで二分探索

INF = float('inf')


def main():
    n, p, k = map(int, input().split())
    r_end = c_end = n
    A = [list(map(int, input().split())) for _ in range(n)]
    x_pos = []
    for r in range(r_end):
        for c in range(c_end):
            if A[r][c] == -1:
                x_pos.append((r, c))

    # 到達可能な都市の数がkより大となる、最大のxを求める
    ok = 0
    ng = 10**11
    while ng - ok > 1:
        mid = (ok + ng) // 2
        set_x(A, x_pos, mid)
        if wf(A, p) > k:
            ok = mid
        else:
            ng = mid
    lo = ok+1

    # 到達可能な都市の数がk-1より大となる、最小のxを求める
    ok = 0
    ng = 10**11
    while ng - ok > 1:
        mid = (ok + ng) // 2
        set_x(A, x_pos, mid)
        if wf(A, p) > k-1:
            ok = mid
        else:
            ng = mid
    hi = ok+1
    ans = hi-lo
    if ans > 10**10:
        ans = 'Infinity'
    print(ans)


def wf(A, p):
    # 隣接行列Aについてワーシャルフロイド法を行う
    # コストp以下で到達可能な組み合わせ数を返す
    n = len(A)
    DP = [[INF] * n for _ in range(n)]
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


def set_x(A, x_pos, x):
    for r, c in x_pos:
        A[r][c] = x


main()
