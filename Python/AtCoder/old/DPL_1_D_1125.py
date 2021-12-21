# LIS
def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    DP = [float('inf')]*n

    ans = 0
    for a in A:
        """
        for i in range(n):
            if DP[i] >= a:
                DP[i] = a
                break
        """
        ok = n
        ng = -1
        while ok - ng > 1:
            mid = (ok + ng)//2
            if DP[mid] >= a:
                ok = mid
            else:
                ng = mid
        DP[ok] = a
        ans = max(ans, ok+1)
    print(ans)


main()
