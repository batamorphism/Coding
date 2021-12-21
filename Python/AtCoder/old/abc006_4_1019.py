def main():
    n = int(input())
    C = [int(input()) for _ in range(n)]
    # カードを何枚か抜いて、残ったカードがソート済みとなればよい
    # すなわち、Cの最長部分増加列の長さを求めればよい

    # LIS
    INF = 10**9
    DP = [INF]*n
    lis_len = 0
    for c in C:
        # DP[i] >= c となる最小のiを求める
        ok = n
        ng = -1
        while ok-ng > 1:
            mid = (ok+ng)//2
            if DP[mid] >= c:
                ok = mid
            else:
                ng = mid
        DP[ok] = c
        lis_len = max(ok+1, lis_len)
    print(n-lis_len)


main()
