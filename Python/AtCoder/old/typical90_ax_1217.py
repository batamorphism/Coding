mod = 10**9+7


# 配るDP
def main():
    n, L = map(int, input().split())

    DP = [0]*(n+L+1)
    DP[0] = 1
    for cur_step in range(1, n+1):
        DP[cur_step] += DP[cur_step-1]
        if cur_step - L >= 0:
            DP[cur_step] += DP[cur_step-L]
        DP[cur_step] %= mod

    ans = DP[n]
    print(ans)


main()
