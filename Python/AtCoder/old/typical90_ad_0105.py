def main():
    n, k = map(int, input().split())
    is_prime = [True]*(n+1)
    factor_cnt = [0]*(n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i]:
            factor_cnt[i] = 1
            for j in range(i*2, n+1, i):
                is_prime[j] = False
                factor_cnt[j] += 1

    ans = 0
    for i in range(2, n+1):
        if factor_cnt[i] >= k:
            ans += 1

    print(ans)


main()
