# 答えで二分探索
INF = float('inf')


def main():
    n = int(input())
    A = list(map(int, input().split()))
    solve1(n, A)
    solve2(n, A)


def solve1(n, A):
    def check(x):
        # 平均値がx以上の場合はTrue
        # A-xの合計が0を超えれば、True
        B = [a-x for a in A]
        # DP[0] = 選ばなかった場合の合計の最大値
        # DP[1] = 選んだ場合の合計の最大値
        DP = [0]*2
        for b_i in B:
            new_DP = [-INF]*2
            # 1. 前回のカードを選んでいなかった場合
            # 今回は必ず選ばなければならない
            new_DP[1] = max(new_DP[1], DP[0]+b_i)
            # 2. 前回のカードを選んでいた場合
            # 今回は選んでも選ばなくてもよい
            new_DP[0] = max(new_DP[0], DP[1])
            new_DP[1] = max(new_DP[1], DP[1]+b_i)
            for is_use in range(2):
                DP[is_use] = new_DP[is_use]
        tot = max(DP)
        if tot >= 0:
            return True
        else:
            return False

    ok = 0
    ng = max(A)+1
    while (ng-ok) > 1e-5:
        mid = (ok+ng) / 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


def solve2(n, A):
    def check(x):
        # 中央値がx以上の場合はTrue
        B = []
        for a in A:
            if a >= x:
                B.append(1)
            else:
                B.append(-1)
        # Bの合計が0より大であれば、中央値はx以上
        # DP[0] = 選ばなかった場合の合計の最大値
        # DP[1] = 選んだ場合の合計の最大値
        DP = [0]*2
        for b_i in B:
            new_DP = [-INF]*2
            # 1. 前回のカードを選んでいなかった場合
            # 今回は必ず選ばなければならない
            new_DP[1] = max(new_DP[1], DP[0]+b_i)
            # 2. 前回のカードを選んでいた場合
            # 今回は選んでも選ばなくてもよい
            new_DP[0] = max(new_DP[0], DP[1])
            new_DP[1] = max(new_DP[1], DP[1]+b_i)
            for is_use in range(2):
                DP[is_use] = new_DP[is_use]
        tot = max(DP)
        if tot > 0:
            return True
        else:
            return False

    ok = 0
    ng = max(A)+1
    while (ng-ok) > 1:
        mid = (ok+ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


main()
