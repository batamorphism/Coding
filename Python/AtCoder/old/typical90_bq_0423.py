def main():
    n, k = map(int, input().split())
    MOD = 10**9+7
    # n-2, n-1の色とnの色が違えばよい
    # n <= 2の場合は、全ての色が異なるため、nCkとおり
    if n <= 2:
        if n == 1:
            ans = k % MOD
            print(ans)
            return
        elif n == 2:
            ans = k*(k-1)
            ans %= MOD
            print(ans)
            return

    # n >= 3の場合は、
    # n-1の答えに、k-2を乗算したものがnの答えである。
    pre_ans = k*(k-1) % MOD
    ans = pre_ans * pow(k-2, n-2, MOD) % MOD
    print(ans)


main()
