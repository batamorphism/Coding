def LIS(A):
    # Aの最長部分増加列の長さを求める
    # Aのindex=kまでを見たときの最長部分増加列の長さをret[k]として
    # ret[k]を返す
    i_end = len(A)
    ret = [0] * i_end
    len_lis = 0
    DP = [float('inf')]*i_end
    for i, a_i in enumerate(A):
        ok = i_end
        ng = -1
        while ok - ng > 1:
            mid = (ok + ng) // 2
            if DP[mid] >= a_i:
                ok = mid
            else:
                ng = mid
        DP[ok] = a_i
        len_lis = max(len_lis, ok + 1)
        ret[i] = len_lis
    return ret


def main():
    n = int(input())
    A1 = list(map(int, input().split()))
    A2 = A1[::-1]
    LIS1 = [0] + LIS(A1)
    LIS2 = [0] + LIS(A2)
    # print(LIS1)
    # print(LIS2)
    ans = 0
    for k in range(1, n+1):
        # LIS[k] = A[:k]の最長部分増加列の長さ
        # print(LIS1[k], LIS2[n-k+1])
        m = LIS1[k] + LIS2[n-k+1] - 1
        ans = max(ans, m)
    print(ans)


main()
