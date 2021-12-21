mod = 10**9+7

def main():
    n = int(input())
    n += 1
    S = input()
    S = '*'+S
    atcoder = '*atcoder'
    len_char = len(atcoder)
    # DP[i][c] := Sをi文字目まで見て、charをc文字目まで見たときの組み合わせ数
    # DP[i][c] = DP[i-1][c] + (DP[i-1][c-1] if S[i] == atcoder[c] else 0)
    DP = [[0]*len_char for _ in range(n)]
    for i in range(n):
        DP[i][0] = 1

    # もらうDP
    for c, char in enumerate(atcoder):
        for i, s in enumerate(S):
            if c == 0 or i == 0:
                continue
            dp = 0
            if s == char:
                dp += DP[i-1][c-1]
            dp += DP[i-1][c]
            DP[i][c] = dp % mod

    print(DP[n-1][len_char-1])


main()
