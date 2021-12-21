def main():
    n = int(input())
    A = list(map(int, input().split()))
    arr_pos = A[:]
    arr_neg = A[::-1]
    arr_pos_lis = lis(arr_pos)
    arr_neg_lis = lis(arr_neg)
    ans = 0
    for sep in range(n):
        # A[:sep+1]のLISの長さ
        lis1 = arr_pos_lis[sep+1]
        # A[sep:]のLISの長さ
        # A[sep]~[n-1]が編集されるため、要素数はn-sep
        lis2 = arr_neg_lis[n-sep]
        ans = max(lis1+lis2-1, ans)
    print(ans)


def test_main():
    print(lis([1, 2, 1, 3]))


def lis(arr: list) -> list:
    """
    arrのLISを計算し
    lis_len[i]=arr[:i]のLISの長さとする
    """
    INF = 10**10
    # DP[i] = arr[:i]の各LISのうち、要素が最小のもの
    i_start = 0
    i_end = len(arr)+1
    lis_len = [0]*i_end
    DP = [INF] * i_end
    for i in range(i_start, i_end):
        if i == 0:
            DP[i] = -INF
            continue
        a = arr[i-1]
        # DPのうち、DP[j]がaより小さく、DP[j+1]がa以上の個所を探す
        ok = 0
        ng = i_end
        while ng-ok > 1:
            mid = (ok+ng)//2
            if DP[mid] < a:
                ok = mid
            else:
                ng = mid
        # DP[ok]<=a and DP[ok+1]>a
        if DP[ok+1] == INF:
            # LISの長さが更新される
            lis_len[i] = lis_len[i-1]+1
        else:
            lis_len[i] = lis_len[i-1]
        DP[ok+1] = a
    return lis_len


main()
