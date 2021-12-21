def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans_list = [0]*n

    # LIS(最長部分増加列)
    # DP[i] = 長さi+1となる増加部分列における最終要素の最小値
    # memo[k] = A[k]まで見た際における、DPの最大長
    A_left = A[:]
    A_right = A[::-1]
    memo_left = LIS(A_left)
    memo_right = LIS(A_right)

    for split in range(n):
        a_left_ind = split
        a_right_ind = n-split-1
        m = memo_left[a_left_ind]+memo_right[a_right_ind]-1
        ans_list[split] = m

    print(max(ans_list))


def LIS(Array: list) -> list:
    """最長部分増加列を求める

    Args:
        Array (list): 最長部分増加列を求める対象

    Returns:
        list: 最長部分増加列の長さ。list[k]でArray[:k+1]までの部分列に対する最長部分増加列の長さとする
    """
    INF = 10**10
    n = len(Array)
    # DP[i] = 長さi+1となる最長部分増加列における最終要素の最小値
    # 各aに対し、DP[i-1]<aとなる最大のiを求める
    # その後、DP[i]=aとする
    DP = [INF]*n
    max_ok = 0
    ret = []
    for a in Array:
        ok = 0
        ng = n
        while ng-ok > 1:
            mid = (ok+ng)//2
            if DP[mid-1] < a:
                ok = mid
            else:
                ng = mid
        max_ok = max(ok, max_ok)
        DP[ok] = a
        ret.append(max_ok+1)
    return ret


main()
