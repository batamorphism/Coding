def main():
    S = input()
    len_S = len(S)
    S = '.'+S
    # DP[i][j]左からi文字選んでchokudaiのうちj文字(0～8)を完成させることができる組み合わせ
    # DP[i][j] = + DP[i-1][j] 一文字前のパターン
    #            + S[i] == C[j]の場合 DP[i-1][j-1]
    DP = [[0]*9 for _ in range(len_S+1)]
    C = '.chokudai'
    for i in range(len_S+1):
        for j in range(9):
            if j == 0:
                DP[i][j] = 1
                continue
            if i == 0:
                DP[i][j] = 0
                continue
            DP[i][j] = DP[i-1][j]
            if S[i] == C[j]:
                DP[i][j] = (DP[i][j]+DP[i-1][j-1]) % (10**9+7)

    print(DP[-1][-1])


main()
