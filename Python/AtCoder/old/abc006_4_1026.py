INF = 10**9

def main():
    # LIS
    n = int(input())
    C = [int(input()) for _ in range(n)]

    DP = [INF]*(n+1)
    DP[0] = -INF
    ans = 0
    for c in C:
        # DP[i] >= c となる最小のi
        ok = n
        ng = 0
        while ok-ng > 1:
            mid = (ok+ng)//2
            if DP[mid] >= c:
                ok = mid
            else:
                ng = mid
        DP[ok] = c
        ans = max(ok, ans)

    print(n-ans)


main()
