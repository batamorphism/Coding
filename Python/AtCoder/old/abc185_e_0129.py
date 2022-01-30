def main():
    a_end, b_end = map(int, input().split())
    A = [-1] + list(map(int, input().split()))
    B = [-1] + list(map(int, input().split()))
    a_end += 1
    b_end += 1
    INF = float('inf')
    DP = [[INF]*b_end for _ in range(a_end)]

    # 配るDP
    for i, a_i in enumerate(A):
        for j, b_j in enumerate(B):
            if i == 0 or j == 0:
                DP[i][j] = max(i, j)
            # 右への遷移
            # a_(i+1)を追加する
            if i+1 < a_end:
                score = DP[i][j] + 1
                DP[i+1][j] = min(DP[i+1][j], score)
            # 下への遷移
            # b_(j+1)を追加する
            if j+1 < b_end:
                score = DP[i][j] + 1
                DP[i][j+1] = min(DP[i][j+1], score)
            # 斜めの遷移
            if i+1 < a_end and j+1 < b_end:
                if A[i+1] == B[j+1]:
                    DP[i+1][j+1] = min(DP[i+1][j+1], DP[i][j])
                else:
                    DP[i+1][j+1] = min(DP[i+1][j+1], DP[i][j]+1)

    ans = DP[a_end-1][b_end-1]
    print(ans)


main()
