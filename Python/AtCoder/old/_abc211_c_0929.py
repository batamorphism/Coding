def main():
    s = input()
    a = 'chokudai'
    p = 10**9+7
    # DP[i][j] = s[:i]とa[:j]について、左からa[0],..,a[j-1]とする組み合わせ数
    # DP[i][j] = s[i-1]==a[j-1]の場合、DP[i-1][j]+DP[i-1][j-1]
    #                  !=      の場合、DP[i-1][j]
    # DP[0][*] = 0
    # DP[*][0] = 1
    max_i = len(s)
    max_j = len(a)
    DP = [[0]*(max_j+1) for _ in range(max_i+1)]
    for i in range(max_i+1):
        for j in range(max_j+1):
            if j == 0:
                DP[i][j] = 1
                continue
            if i == 0:
                DP[i][j] = 0
                continue
            if s[i-1] == a[j-1]:
                DP[i][j] = (DP[i-1][j]+DP[i-1][j-1]) % p
            else:
                DP[i][j] = DP[i-1][j] % p

    print(DP[-1][-1] % p)


main()
