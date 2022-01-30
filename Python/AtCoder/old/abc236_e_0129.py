def main():
    n = int(input())
    A = list(map(int, input().split()))
    solve_mean(n, A)
    solve_mid(n, A)


def solve_mean(n, A):
    # 答えで二分探索
    def B(i, mid):
        """ 次に相当するものを返す
        B = [-1]
        for a in A:
            B.append(a-mid)
        """
        if i == 0:
            raise
        return A[i-1]-mid

    def check(A, mid):
        # Bの合計が0以上ならば、平均値はmid以上であり、okを返す
        # Bの選び方は、iを選んだらi+1は選ばなくてもよい
        DP = [[0]*2 for _ in range(n+1)]
        # DP[i][0] = i番目を選んでない状態における、Bの合計
        # DP[i][1] = i番目を選んだ状態における、Bの合計
        # 貰うDP
        for i in range(1, n+1):
            # 1-indexed
            b_i = B(i, mid)
            # i番目を選ばない場合
            # i-1番目は選んでいなければならない
            dp = DP[i-1][1]
            DP[i][0] = dp

            # i番目を選ぶ場合
            # i-1番目は選ばれていても、選んでいてもよい
            dp = DP[i-1][0] + b_i
            dp = max(dp, DP[i-1][1] + b_i)
            DP[i][1] = dp
        avg = max(DP[n])
        if avg >= 0:
            return True
        else:
            return False
    ok = 0
    ng = max(A)+1
    while abs(ng - ok) > 1e-6:
        mid = (ok + ng) / 2
        if check(A, mid):
            ok = mid
        else:
            ng = mid
    print(ok)


def solve_mid(n, A):
    # 答えで二分探索
    def B(i, mid):
        """ 次に相当するものを返す
        B = [-1]
        for a in A:
            B.append(a-mid)
        """
        if i == 0:
            raise
        if A[i-1] >= mid:
            ret = 1
        else:
            ret = -1
        return ret

    def check(A, mid):
        # Bの合計が0以上ならば、中央値はmid以上であり、okを返す
        # Bの選び方は、iを選んだらi+1は選ばなくてもよい
        DP = [[0]*2 for _ in range(n+1)]
        # DP[i][0] = i番目を選んでない状態における、Bの合計
        # DP[i][1] = i番目を選んだ状態における、Bの合計
        # 貰うDP
        for i in range(1, n+1):
            # 1-indexed
            b_i = B(i, mid)
            # i番目を選ばない場合
            # i-1番目は選んでいなければならない
            dp = DP[i-1][1]
            DP[i][0] = dp

            # i番目を選ぶ場合
            # i-1番目は選ばれていても、選んでいてもよい
            dp = DP[i-1][0] + b_i
            dp = max(dp, DP[i-1][1] + b_i)
            DP[i][1] = dp
        avg = max(DP[n])
        if avg > 0:
            return True
        else:
            return False
    ok = 0
    ng = max(A)+1
    check(A, 5)
    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        if check(A, mid):
            ok = mid
        else:
            ng = mid
    print(ok)


main()
