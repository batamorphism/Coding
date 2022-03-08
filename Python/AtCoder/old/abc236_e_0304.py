# 答えで二分探索
def main():
    n = int(input())
    A = list(map(int, input().split()))
    print(solve1(n, A))
    print(solve2(n, A))


def solve1(n, A):
    # 選んだカードの整数の平均値としてあり得る最大値
    INF = float('inf')

    def check(mid):
        # Aの平均値がmid以上である場合True
        # BをA-midとする。
        # DP[i]は、Bのi番目のカードを選んだ場合の、総和の最大値とする
        B = [A[i] - mid for i in range(n)]
        DP = [[-INF]*2 for _ in range(n+1)]
        DP[0][1] = 0
        for i, b_i in enumerate(B, 1):
            # b_iを採用する場合
            DP[i][1] = max(DP[i-1][0] + b_i, DP[i-1][1] + b_i)
            # b_iを採用しない場合
            DP[i][0] = DP[i-1][1]
        sum_ = max(DP[n])
        if sum_ >= 0:
            return True
        else:
            return False

    ok = min(A)-1
    ng = max(A)+1
    while ng - ok > 1e-5:
        mid = (ok+ng)/2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok


def solve2(n, A):
    # 選んだカードの整数の中央値としてあり得る最大値
    INF = float('inf')

    def check(mid):
        # Aの中央値がmid以上である場合True
        # DP[i]は、Bのi番目のカードを選んだ場合の、総和の最大値とする
        B = []
        for a_i in A:
            if a_i >= mid:
                B.append(1)
            else:
                B.append(-1)
        DP = [[-INF]*2 for _ in range(n+1)]
        DP[0][1] = 0
        for i, b_i in enumerate(B, 1):
            # b_iを採用する場合
            DP[i][1] = max(DP[i-1][0] + b_i, DP[i-1][1] + b_i)
            # b_iを採用しない場合
            DP[i][0] = DP[i-1][1]
        sum_ = max(DP[n])
        if sum_ > 0:
            # mid以上の数が、半分より多い場合はOK、ちょうど半分はだめ
            return True
        else:
            return False

    ok = min(A)-1
    ng = max(A)+1
    while ng - ok > 1:
        mid = (ok+ng)//2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok


main()
