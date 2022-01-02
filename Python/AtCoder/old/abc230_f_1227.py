from collections import defaultdict
mod = 998244353


def main():
    n = int(input())
    A = list(map(int, input().split()))

    def m1():
        return -1

    d = defaultdict(m1)

    DP = [0] * (n+1)
    DP[0] = 1
    sum_a = 0
    for i, a in enumerate(A):
        sum_a += a
        j = d[sum_a]
        DP[i+1] = DP[i]*2
        if j != -1:
            DP[i+1] -= DP[j]
        DP[i+1] %= mod
        d[sum_a] = i
    ans = DP[n-1]
    print(ans)


main()
