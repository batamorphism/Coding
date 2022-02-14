# LIS
def main():
    n = int(input())
    A = list(map(int, input().split()))
    lis_le = LIS(A)
    lis_ri = LIS(A[::-1])
    lis_ri = lis_ri[::-1]
    m = -1
    for i in range(n):
        # A[:i]までのLIS
        m_le = lis_le[i]
        # A[i:]のLIS
        m_ri = lis_ri[i]
        m = max(m, m_le + m_ri - 1)
    print(m)


def LIS(A):
    # Aの最長増加部分列を求める
    n = len(A)
    INF = float('inf')
    DP = [INF]*(n+1)
    DP[0] = -INF
    ret = [0]*n

    for i, a_i in enumerate(A):
        # DP[i] < a かつ DP[i+1] >= a であるような i を探す
        # DP[i+1] = aとする
        ok = 0
        ng = n
        while abs(ng-ok) > 1:
            mid = (ok+ng)//2
            if DP[mid] < a_i:
                ok = mid
            else:
                ng = mid
        DP[ok+1] = a_i
        ret[i] = ok+1

    return ret


main()
