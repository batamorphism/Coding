# 左2つと違う色で塗る
# n = 1 -> k
# n = 2 -> k*(k-1)
# n = 3 -> k*(k-1)*(k-2)
# n = 4 -> k*(k-1)*(k-2)*(k-2)
def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7

    if n == 1:
        print(k % mod)
        return
    elif n == 2:
        print((k*(k-1)) % mod)
        return

    ans = k*(k-1)*pow(k-2, n-2, mod)
    ans %= mod
    print(ans)


main()
