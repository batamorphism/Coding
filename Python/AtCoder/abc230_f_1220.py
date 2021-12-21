# DP[i]
# a_iまで見たときに考えられる組み合わせ数
# DP[0] = 0
# DP[1] = 1
# DP[i] = DP[i-1] <- i-1とiに区切りを入れる
#       + DP[i-1] <- i-1とiに区切りを入れる
#       - DP[j-1] <- j～iの和が0の時、ダブルカウント
from collections import defaultdict
mod = 998244353


def main():
    n = int(input())
    DP = [0] * (n + 1)
    DP[1] = 1
    f = [0]*(n+1)
    d = defaultdict(int)
    A = [0] + list(map(int, input().split()))

    sum_a = 0
    for i, a in enumerate(A):
        sum_a += a
        f[i] = d[sum_a]
        d[sum_a] = i

    for i in range(2, n+1):
        DP[i] = DP[i-1]*2 - DP[f[i-1]]
        DP[i] %= mod

    print(DP[n])


main()
