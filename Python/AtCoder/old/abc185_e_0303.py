# LCM
def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # DP[i][j] := Aのi番目と、Bのj番目まで見たときの答え
    INF = float('inf')
    DP = [[INF] * (m + 1) for _ in range(n + 1)]

    DP[0][0] = 0
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                DP[i][j] = j
                continue
            if j == 0:
                DP[i][j] = i
                continue
            a_i = A[i-1]
            b_j = B[j-1]
            if a_i == b_j:
                DP[i][j] = DP[i-1][j-1]
            else:
                DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1

    ans = DP[n][m]
    print(ans)


main()
