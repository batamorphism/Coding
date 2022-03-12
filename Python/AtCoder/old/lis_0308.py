def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    ans = lis(A)
    print(ans)


def lis(A):
    INF = float('inf')
    n = len(A)
    DP = [INF]*(n+10)
    DP[0] = -INF
    ans = 0
    for a_k in A:
        # DP[i] < a_kとなる最大のiを求める
        # このiの次に、a_kを編集する
        ok = 0
        ng = n+1
        while ng - ok > 1:
            mid = (ok+ng)//2
            if DP[mid] < a_k:
                ok = mid
            else:
                ng = mid
        DP[ok+1] = a_k
        ans = max(ans, ok+1)
    return ans


main()
