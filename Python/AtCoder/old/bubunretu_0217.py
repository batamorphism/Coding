from collections import defaultdict


def main():
    s = input()
    n = len(s)
    # dp[i] = i文字目まで使い、かつi文字目を使った場合の、部分列として考えられるものの個数
    dp = [0]*(n+1)
    sum_dp = [0]*(n+1)
    pos = defaultdict(lambda: -1)
    dp[0] = 1
    sum_dp[0] = 1

    # 貰うDP
    for cur_i, s_i in enumerate(s, 1):
        bef_i = pos[s_i]
        cur_dp = 0
        if bef_i == -1:
            cur_dp = sum_dp[cur_i-1]
        else:
            cur_dp = sum_dp[cur_i-1] - sum_dp[bef_i-1]
        dp[cur_i] = cur_dp
        sum_dp[cur_i] = sum_dp[cur_i-1] + cur_dp
        pos[s_i] = cur_i

    ans = sum(dp)
    print(ans)


main()
