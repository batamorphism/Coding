# 答えで二分探索
def main():
    n = int(input())
    A = list(map(int, input().split()))
    print(solve1(A, n))
    print(solve2(A, n))


def solve1(A, n):
    INF = float('inf')

    def check(mid):
        B = []
        for a in A:
            B.append(a-mid)
        # Bの総和が0を超えたら、平均値はmid以上である。
        # DP[i][01] = i番目を使う場合とつかわない場合それぞれのBの総和
        DP = [[-INF]*2 for _ in range(n+1)]
        DP[0][1] = 0
        for i in range(1, n+1):
            b_i = B[i-1]
            # b_iを使わない場合
            DP[i][0] = DP[i-1][1]
            # b_iを使う場合
            DP[i][1] = max(DP[i-1][0]+b_i, DP[i-1][1]+b_i)
        sum_val = max(DP[n])
        return sum_val >= 0

    ok = 0
    ng = max(A) + 1
    while ng - ok > 1e-5:
        mid = (ok + ng)/2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok


def solve2(A, n):
    INF = float('inf')

    def check(mid):
        # mid以上の要素が過半数(同数は駄目)を占めるかを確認すればよいので
        # mid以上の要素を+1, 未満を-1として、総和が0を超えればよい
        B = []
        for a in A:
            if a >= mid:
                B.append(1)
            else:
                B.append(-1)
        # Bの総和が0を超えたら、平均値はmid以上である。
        # DP[i][01] = i番目を使う場合とつかわない場合それぞれのBの総和
        DP = [[-INF]*2 for _ in range(n+1)]
        DP[0][1] = 0
        for i in range(1, n+1):
            b_i = B[i-1]
            # b_iを使わない場合
            DP[i][0] = DP[i-1][1]
            # b_iを使う場合
            DP[i][1] = max(DP[i-1][0]+b_i, DP[i-1][1]+b_i)
        sum_val = max(DP[n])
        return sum_val > 0

    ok = 0
    ng = max(A) + 1
    while ng - ok > 1:
        mid = (ok + ng)//2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok


main()
