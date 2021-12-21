INF = 10**9


def lis(A):
    # A[:i]まで見たときのLISの長さを返す

    n = len(A)
    # DP[i] = 長さi-1の、Aの最長部分増加列の末尾で最小のもの
    ret = [0]*n
    DP = [INF]*n
    lis_len = 0
    for i, a in enumerate(A):
        """
        次を効率化
        for i in range(n+1):
            if DP[i] >= a:
                DP[i] = a
                continue
        """
        ng = -1
        ok = n-1
        while ok-ng > 1:
            mid = (ok+ng)//2
            if DP[mid] >= a:
                ok = mid
            else:
                ng = mid
        DP[ok] = a
        lis_len = max(ok, lis_len)
        ret[i] = lis_len+1
    return ret


def main():
    n = int(input())
    A_nor = list(map(int, input().split()))
    A_rev = A_nor[::-1]
    A_nor_lis = lis(A_nor)
    A_rev_lis = lis(A_rev)
    ans = 0
    for sep in range(n):
        b_len = A_nor_lis[sep]+A_rev_lis[n-sep-1]-1
        ans = max(b_len, ans)
    print(ans)


main()
