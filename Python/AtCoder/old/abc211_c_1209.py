mod = 10**9 + 7


def main():
    text1 = 'chokudai'
    text2 = input()
    text1 = '*' + text1
    text2 = '*' + text2

    n1 = len(text1)
    n2 = len(text2)
    DP = [[0] * n2 for _ in range(n1)]

    for i2 in range(n2):
        DP[0][i2] = 1

    for i1 in range(1, n1):
        for i2 in range(1, n2):
            dp1 = DP[i1][i2-1]
            dp2 = 0
            if text1[i1] == text2[i2]:
                dp2 = DP[i1-1][i2-1] + dp1
            DP[i1][i2] = max(dp1, dp2) % mod

    ans = DP[n1-1][n2-1]

    print(ans)


main()
