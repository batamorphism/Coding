# c_iを塗り替える場合と、塗り替えない場合を考える
from collections import defaultdict


def main():
    MOD = 10**9+7
    n = int(input())
    C = [0] + [int(input()) for _ in range(n)]

    d = defaultdict(lambda: -1)
    DP = [0] * (n+1)
    DP[0] = 1
    for i, c_i in enumerate(C[1:], 1):
        dp = DP[i-1]
        j = d[c_i]
        if j != -1 and j < i-1:
            dp += DP[j]
        DP[i] = dp % MOD
        d[c_i] = i

    ans = DP[-1]
    print(ans)


main()
