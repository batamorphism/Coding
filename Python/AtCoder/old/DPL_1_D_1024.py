INF = 10**10


def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]
    DP = [INF]*(n+1)
    DP[0] = -INF

    ans = 0
    for a in A:
        # DP[i] >= aとなる最小のiを求める
        ok = n
        ng = -1
        while ok - ng > 1:
            mid = (ok+ng)//2
            if DP[mid] >= a:
                ok = mid
            else:
                ng = mid
        DP[ok] = a
        ans = max(ok, ans)

    print(ans)


main()
