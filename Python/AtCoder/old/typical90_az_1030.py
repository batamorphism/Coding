mod = 10**9+7
# SUM(X1*...*Xn)
# SUM(X1)*...*SUM(Xn)


def main():
    n = int(input())
    ans = 1
    for _ in range(n):
        A = list(map(int, input().split()))
        ans *= sum(A)
        ans %= mod
    print(ans)


main()
