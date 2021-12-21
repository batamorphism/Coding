INF = 10**9


def main():
    n, m = map(int, input().split())
    C = list(map(int, input().split()))
    # x円支払うときの、最小の枚数をDP[x]とする
    # DP[x] = DP[x-C[i]]+1のmin
    DP = [0]*(n+1)
    for x in range(1, n+1):
        dp = INF
        for c in C:
            if x-c < 0:
                continue
            cnt = DP[x-c]+1
            dp = min(cnt, dp)
        DP[x] = dp

    print(DP[n])


main()
