def main():
    room, k = map(int, input().split())
    MOD = 10**9+7

    # 誰もいない部屋の数をemptyとする
    # 0 <= empty <= min(room-1, k)
    # emptyの選び方は、(room)C(empty)
    # empty人が移動したものと考えてよい
    # empty人は、room-empty個の部屋に移動する
    # 移動した後の人数の組み合わせ数は、
    # (room-empty)H(empty)

    nr_end = 2*room+1
    factorial_memo = [1] * nr_end
    rev_factorial_memo = [1] * nr_end
    for nr in range(1, nr_end):
        factorial_memo[nr] = factorial_memo[nr-1] * nr % MOD
        rev_factorial_memo[nr] = rev(factorial_memo[nr], MOD)

    def factorial(n):
        return factorial_memo[n]

    def rev_factorial(n):
        return rev_factorial_memo[n]

    def nCr(n, r):
        # n!/r!(n-r)!
        return factorial(n) * rev_factorial(r) * rev_factorial(n-r) % MOD

    def nHr(n, r):
        # (n+r-1)Cr
        return nCr(n+r-1, r)

    ans = 0
    for empty in range(min(room-1, k)+1):
        ans += nCr(room, empty)*nHr(room-empty, empty)
        ans %= MOD
    print(ans)


def rev(val, mod):
    return pow(val, mod-2, mod)


main()
