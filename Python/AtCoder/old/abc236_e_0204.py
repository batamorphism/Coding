# 答えで2分探索
INF = float('inf')


def main():
    n = int(input())
    A = list(map(int, input().split()))

    print(solve_1(A, n))
    print(solve_2(A, n))


def solve_1(A, n):
    # Aから選んだカードの整数の平均値としてありうる最大値を求める

    def check(mid):
        # Aの部分列の平均がmid以上になるか
        B = A[:]
        B = [a - mid for a in A]
        # Bの部分列の総和が0以上になるか
        # DP[i][01] = i番目を選ばない場合の総和の最大値と、選ぶ場合の総和の最大値
        DP = [[-INF]*2 for _ in range(n+1)]
        DP[0][1] = 0
        for i, b_i in enumerate(B, 1):
            # i番目を選ばない場合
            # i-1番目は選んでなければならない
            DP[i][0] = DP[i-1][1]
            # i番目を選ぶ場合
            DP[i][1] = max(DP[i-1][0] + b_i, DP[i-1][1] + b_i)
        ans = max(DP[n])
        return ans >= 0

    ok = 0
    ng = max(A)+1
    while ng - ok > 1e-5:
        mid = (ok + ng) / 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok


def solve_2(A, n):
    # Aから選んだカードの整数の中央としてありうる最大値を求める

    def check(mid):
        # Aの部分列の中央値がmid以上になるか
        B = []
        for a in A:
            if a - mid >= 0:
                B.append(1)
            else:
                B.append(-1)
        # Bの部分列の総和が0以上になるか
        # DP[i][01] = i番目を選ばない場合の総和の最大値と、選ぶ場合の総和の最大値
        DP = [[-INF]*2 for _ in range(n+1)]
        DP[0][1] = 0
        for i, b_i in enumerate(B, 1):
            # i番目を選ばない場合
            # i-1番目は選んでなければならない
            DP[i][0] = DP[i-1][1]
            # i番目を選ぶ場合
            DP[i][1] = max(DP[i-1][0] + b_i, DP[i-1][1] + b_i)
        ans = max(DP[n])
        return ans > 0

    check(5)
    ok = 0
    ng = max(A)+1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok


main()
