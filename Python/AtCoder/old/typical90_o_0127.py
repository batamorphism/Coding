def main():
    n = int(input())
    MOD = 10**9 + 7

    factorial = [1] * (n + 1)
    rev_factorial = [1] * (n + 1)
    for i in range(1, n+1):
        factorial[i] = (factorial[i-1] * i) % MOD
        rev_factorial[i] = pow(factorial[i], MOD-2, MOD)

    def comb(n, r):
        # n! / r!(n-r)!
        return (factorial[n] * rev_factorial[r] * rev_factorial[n-r]) % MOD

    for k in range(1, n+1):
        ans = 0
        for r in range(1, n+1):
            nn = n-(k-1)*(r-1)
            if nn <= 0:
                break
            if nn < r:
                break
            ans += comb(nn, r)
            ans %= MOD
        print(ans)


main()
