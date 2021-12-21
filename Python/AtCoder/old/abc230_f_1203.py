# (n-1)Ck をk=0～n-1について加算
mod = 998244353


def main():
    n = int(input())
    A = list(map(int, input().split()))
    cnt0 = A.count(0)
    # nCk = n! / (k! * (n-k)!)
    fractions = [1] * (n + 1)
    for i in range(1, n + 1):
        fractions[i] = fractions[i - 1] * i
        fractions[i] %= mod

    ans = 0
    for k in range(n):
        ans += fractions[n-1]*rev(fractions[k])*rev(fractions[n-k-1])
        ans %= mod
    # ans = fractions[n-1]*rev(fractions[k])*rev(fractions[n-k-1])
    print(ans)


def rev(val):
    return pow(val, mod - 2, mod)


main()
