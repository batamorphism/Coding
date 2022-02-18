# 答えへの貢献度
def main():
    n = int(input())
    A = [(-1, -1)] + list(tuple(map(int, input().split())) for _ in range(n))
    x_end = 101

    # DP[i][x] := i番目まで見たときの、xより大きい数が平均何個あるか
    DP = [[0]*x_end for _ in range(n+1)]
    ans = 0

    # 貰うDP
    for pre_i, (pre_lo, pre_hi) in enumerate(A[:-1]):
        cur_i = pre_i + 1
        cur_lo, cur_hi = A[cur_i]

        for cur_x in range(x_end):
            if cur_x > cur_hi:
                DP[cur_i][cur_x] = DP[pre_i][cur_x]
            elif cur_lo <= cur_x <= cur_hi:
                cur_dp = DP[pre_i][cur_x] + (cur_hi-cur_x)/(cur_hi-cur_lo+1)
                DP[cur_i][cur_x] = cur_dp
                ans += DP[pre_i][cur_x]/(cur_hi-cur_lo+1)
            else:
                DP[cur_i][cur_x] = DP[pre_i][cur_x] + 1

    print(ans)


main()
