def main():
    n = int(input())
    A = list(map(int, input().split()))
    DP = [[0]*n for _ in range(10)]
    # DP[k][i] = i回操作した時に、左端がkとなる組み合わせ
    # i = 0~n-1
    # DP[k][i] = SUM(DP[f][i-1]) ただし、fはFの操作でkになるもの
    #          = SUM(DP[g][i-1]) ただし、gはGの操作でkになるもの
    p = 998244353
    for i in range(n):
        for k in range(10):
            if i == 0:
                if A[0] == k:
                    DP[k][i] = 1
                else:
                    DP[k][i] = 0
                continue
            for f in range(10):
                if (f+A[i]) % 10 == k:
                    DP[k][i] += DP[f][i-1] % p
            for g in range(10):
                if (g*A[i]) % 10 == k:
                    DP[k][i] += DP[g][i-1] % p

    for k in range(10):
        print(DP[k][n-1] % p)


main()
