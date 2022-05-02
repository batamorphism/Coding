from collections import defaultdict
MOD = 998244353


def main():
    n = int(input())
    A = [0] + list(map(int, input().split()))

    f = [0] * (n+1)
    d = defaultdict(int)
    sum_a = 0

    for i, a_i in enumerate(A):
        sum_a += a_i
        f[i] = d[sum_a]
        d[sum_a] = i

    DP = [0] * (n+1)
    DP[1] = 1
    for i in range(1, n):
        DP[i+1] = (DP[i]*2 - DP[f[i]]) % MOD

    print(DP[-1])


main()
