def main():
    a_end, b_end = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    a_end += 1
    b_end += 1

    INF = float('inf')
    DP = [[INF] * b_end for _ in range(a_end)]
    for i, a_i in enumerate(A):
        for j, b_j in enumerate(B):
            if i == 0 or j == 0:
                DP[i][j] = max(i, j)
                continue
            dp1 = DP[i-1][j] + 1
            dp2 = DP[i][j-1] + 1
            dp3 = DP[i-1][j-1] + (0 if a_i == b_j else 1)
            DP[i][j] = min(dp1, dp2, dp3)

    ans = DP[-1][-1]
    print(ans)


main()
