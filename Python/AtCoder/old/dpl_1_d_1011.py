def main():
    # LIS
    n = int(input())
    A = [int(input()) for _ in range(n)]
    INF = 10**10
    DP = [INF]*n  # Aの長さiの増加部分列のうち、末尾が最小となるもの
    ans = 0
    for a in A:
        # DP[i] >= aを満たす最小のiを探す
        ok = n
        ng = -1
        while ok-ng > 1:
            mid = (ok+ng)//2
            if DP[mid] >= a:
                ok = mid
            else:
                ng = mid
        DP[ok] = a
        ans = max(ok+1, ans)
        """ 上はこのコードの代替
        for i in range(n):
            if DP[i] >= a:
                ans = max(i+1, ans)
                DP[i] = a
                break
        """
    print(ans)


main()
