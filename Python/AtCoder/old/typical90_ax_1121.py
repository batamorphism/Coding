# DAG、DP
# x段目にいるとき、x+1、x+Lに行くパターンが+DP[x]される
# 配るDP
mod = 10**9+7


def main():
    n, L = map(int, input().split())
    DP = [0]*(n+L+10)
    DP[0] = 1
    for pre in range(n+1):
        DP[pre] %= mod
        DP[pre+1] += DP[pre]
        DP[pre+L] += DP[pre]

    print(DP[n] % mod)


main()
