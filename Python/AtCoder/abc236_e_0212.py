def main():
    n = int(input())
    A = list(map(int, input().split()))
    solve1(A, n)
    solve2(A, n)


def solve1(A, n):
    # 平均値の最大値
    INF = float('inf')

    def check(mid):
        # 平均値がmid以上である場合ok
        B = [a-mid for a in A]
        # Bから部分列をとり、0以上となればok
        DP = [[-INF]*2 for _ in range(n+1)]
        # DP[i][01] i番目のカードを使った場合の総和の最大値
        DP[0][1] = 0
        for i, b_i in enumerate(B, 1):
            # 1-indexed
            # もらうDP
            # i番目を使わない場合
            DP[i][0] = DP[i-1][1]
            # i番目を使う場合
            DP[i][1] = max(DP[i-1][0] + b_i, DP[i-1][1] + b_i)
        sum_ = max(DP[n])
        return sum_ >= 0

    ok = 0
    ng = max(A) + 1
    while ng - ok > 1e-5:
        mid = (ok + ng) / 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


def solve2(A, n):
    # 中央の最大値
    INF = float('inf')

    def check(mid):
        # mid以上の数がmid未満の数より多ければok
        # 同数はng
        B = []
        for a in A:
            if a >= mid:
                B.append(1)
            else:
                B.append(-1)
        # Bから部分列をとり、0以上となればok
        DP = [[-INF]*2 for _ in range(n+1)]
        # DP[i][01] i番目のカードを使った場合の総和の最大値
        DP[0][1] = 0
        for i, b_i in enumerate(B, 1):
            # 1-indexed
            # もらうDP
            # i番目を使わない場合
            DP[i][0] = DP[i-1][1]
            # i番目を使う場合
            DP[i][1] = max(DP[i-1][0] + b_i, DP[i-1][1] + b_i)
        sum_ = max(DP[n])
        return sum_ > 0

    ok = 0
    ng = max(A) + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


main()
