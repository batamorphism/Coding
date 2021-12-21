def main():
    search_text = '*atcoder'
    mod = 10**9 + 7

    n = int(input())
    text = '*' + input()
    r_end = len(search_text)
    c_end = len(text)
    DP = [[0]*(c_end) for _ in range(r_end)]

    for c in range(c_end):
        DP[0][c] = 1

    for r in range(1, r_end):
        for c in range(1, c_end):
            dp1 = DP[r][c-1]
            dp2 = 0
            if search_text[r] == text[c]:
                dp2 = DP[r-1][c-1]
            DP[r][c] = (dp1 + dp2) % mod

    ans = DP[-1][-1]
    print(ans)


main()
