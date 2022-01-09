# O(n*m)は間に合う
# DP[val] = val円ちょうどを支払う場合の、コインの最小の枚数
# DP[0][0] = 1
def main():
    n, _ = map(int, input().split())
    C = list(map(int, input().split()))
    INF = float('inf')

    DP = [INF] * (n+1)
    DP[0] = 0

    for val in range(1, n+1):
        dp = INF
        for c in C:
            if val - c < 0:
                continue
            bef_val = val - c
            dp = min(DP[bef_val] + 1, dp)
        DP[val] = dp

    ans = DP[-1]
    print(ans)


main()
