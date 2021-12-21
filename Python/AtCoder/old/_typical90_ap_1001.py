def main():
    k = int(input())
    p = 10**9+7
    # DP[n][i] = n桁の数値について、各桁の数値の和がiである者の組み合わせ数
    # DP[n][i] = DP[n-1][i-1]+...+DP[n-1][i-9]
    # DP[1][i] = 1 (1<=i<=9)
    # DP[i] = DP[i-1]+...+DP[i-9]
    DP = [0]*(k+1)
    DP[0] = 1

    for i in range(1, k+1):
        for di in range(1, 10):
            if i-di < 0:
                break
            DP[i] += DP[i-di] % p

    ans = 0
    if k % 9 == 0:
        ans = DP[k]
    print(ans % p)


main()
