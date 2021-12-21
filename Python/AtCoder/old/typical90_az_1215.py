# E(X*Y) = E(X)*E(Y)
# S(X*Y) = S(X)*S(Y)
def main():
    mod = 10**9 + 7

    n = int(input())
    sum_of = []
    for _ in range(n):
        s = sum(map(int, input().split()))
        s %= mod
        sum_of.append(s)

    ans = 1
    for val in sum_of:
        ans *= val
        ans %= mod
    print(ans)


main()
