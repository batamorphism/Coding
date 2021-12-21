mod = 10**9+7


def main():
    # E[X]*E[Y] = E[XY]
    n = int(input())
    ans = 1
    for _ in range(n):
        A = list(map(int, input().split()))
        ans *= sum(A)
        ans %= mod
    print(ans)


main()
