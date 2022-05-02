from collections import defaultdict
MOD = 998244353


def main():
    n = int(input())
    A = [0] + list(map(int, input().split()))

    # f[i] = (f[i], i]の総和が0となる
    f = [-1] * (n+1)
    d = defaultdict(int)
    a_sum = 0
    for i, a_i in enumerate(A):
        a_sum += a_i
        bef_i = d[a_sum]
        f[i] = bef_i
        d[a_sum] = i

    DP = [0] * (n+1)
    DP[1] = 1
    # 配るDP
    for i, a_i in enumerate(A[1:-1], 1):
        bef_i = f[i]
        # (bef_i, i]の総和が0
        DP[i+1] = DP[i]*2
        DP[i+1] -= DP[bef_i]
        DP[i+1] %= MOD

    ans = DP[-1]
    print(ans)


main()
