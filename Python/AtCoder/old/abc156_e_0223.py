def nCr(n, r):
    # n!/r!/(n-r)!
    return (factorial[n]*rev_factorial[r]*rev_factorial[n-r]) % MOD


def nHr(n, r):
    # (n+r-1)Cr
    return nCr(n+r-1, r)


def rev(val):
    return pow(val, MOD-2, MOD)


def main():
    n, k = map(int, input().split())

    ans = 0
    for zero in range(min(k+1, n)):
        ans += nCr(n, zero) * nHr(n-zero, zero)
        ans %= MOD

    print(ans)


MOD = 10**9 + 7
num_end = 10**5*5
factorial = [1]*num_end
rev_factorial = [1]*num_end
for num in range(1, num_end):
    factorial[num] = (num * factorial[num-1]) % MOD
    rev_factorial[num] = rev(factorial[num])


main()
