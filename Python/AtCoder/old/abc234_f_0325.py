from collections import Counter


def main():
    S = list(input())
    S = [c2i(c) for c in S]
    cnt_of = Counter(S)
    n = len(S)
    MOD = 998244353

    # Setup nHr
    factorial_end = (n+n-1)+1
    factorial = [1]*factorial_end
    rev_factorial = [1]*factorial_end
    for i in range(1, factorial_end):
        factorial[i] = (factorial[i-1] * i) % MOD
        rev_factorial[i] = pow(factorial[i], MOD-2, MOD)

    def nCr(n, r):
        # nCr = n! / (r! * (n-r)!)
        return factorial[n] * rev_factorial[r] * rev_factorial[n-r] % MOD

    def nHr(n, r):
        # nHr = (n+r-1)Cr
        return nCr(n+r-1, r)

    DP = [0]*(n+1)
    DP[0] = 1  # 0文字

    for key, cnt in cnt_of.items():
        # pre_len文字に
        # 新たにcnt文字を挟み込む
        # (pre_len+1)H(cur_cnt)
        # cur_len = pre_len + cur_cnt
        # となり、cur_len文字使った場合の組み合わせ数がこれで更新される
        new_DP = [0]*(n+1)
        for pre_len in range(n+1):
            if DP[pre_len] == 0:
                continue
            for cur_cnt in range(cnt+1):
                cur_len = pre_len + cur_cnt
                if cur_len > n:
                    break
                new_DP[cur_len] += DP[pre_len] * nHr(pre_len+1, cur_cnt)
        for i in range(n+1):
            DP[i] = new_DP[i] % MOD

    ans = sum(DP)-1
    ans %= MOD
    print(ans)


def c2i(c):
    return ord(c) - ord('a')


main()
