def main():
    INF = 10**9
    # 区間DP
    n = int(input())
    i_end = 2*n+1
    A = list(map(int, input().split()))
    DP = [[INF]*i_end for _ in range(i_end)]
    for diff in range(i_end):
        for L in range(i_end):
            R = L+diff
            if R >= i_end:
                break
            if diff == 0:
                DP[L][R] = 0
                continue
            dp = INF
            for sep in range(L, R):
                dp = min(DP[L][sep]+DP[sep][R], dp)
            if (L+1) < i_end and R-1 >= 0:
                dp = min(DP[L+1][R-1]+abs(A[L]-A[R-1]), dp)
            DP[L][R] = dp

    print(DP[0][i_end-1])


main()
