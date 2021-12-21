mod = 10**9 + 7


def main():
    n, k = map(int, input().split())
    # k*(k-1)*(k-2)...*(k-2)
    # k*(k-1)*pow(k-2, n-2)
    # ただし、n <= 2の時は別計算
    if n == 1:
        ans = k % mod
    elif n == 2:
        ans = k*(k-1) % mod
    else:
        ans = k*(k-1)*pow(k-2, n-2, mod) % mod

    print(ans)


main()
