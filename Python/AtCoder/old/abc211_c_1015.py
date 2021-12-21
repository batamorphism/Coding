mod = 10**9+7


def main():
    S = input()
    # DP
    search = 'chokudai'
    S = '*'+S
    search = '*'+search
    # DP[k][n] : n文字目まで見たときに、searchの1～k文字を選ぶ方法が何通りあるか
    k_end = len(search)
    n_end = len(S)
    DP = [[0]*n_end for _ in range(k_end)]
    for k in range(k_end):
        for n in range(n_end):
            if k == 0:
                DP[k][n] = 1
                continue
            if n == 0:
                DP[k][n] = 0
                continue
            if search[k] == S[n]:
                DP[k][n] = (DP[k-1][n]+DP[k][n-1]) % mod
            else:
                DP[k][n] = DP[k][n-1]

    print(DP[-1][-1] % mod)


main()

#  *aabcbc
# *1111111
# a0122222
# b0002244
# c0000226
