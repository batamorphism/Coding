def main():
    # 1-indexed
    n_end, k = map(int, input().split())
    n_end += 1  # 1-indexed

    A = [0] + [int(input()) for _ in range(n_end-1)]

    # S[ri] = A[1]+...+A[ri]
    S = A
    for i in range(1, n_end):
        S[i] += S[i-1]

    # T[ri] = S[ri] - k * ri
    T = S
    for i in range(n_end):
        T[i] -= k * i

    # T[ri] >= T[le]かつ、ri > leを満たすペアの数を求める

    # 座圧
    zipper = {t: i for i, t in enumerate(sorted(list(set(T))))}
    T = [zipper[t] for t in T]

    bit_end = n_end + 10
    bit_dat = [0] * bit_end

    def add(pos, val):
        pos += 1
        while pos < bit_end:
            bit_dat[pos] += val
            pos += (pos & -pos)

    def get_sum(pos):
        pos += 1
        ret = 0
        while pos > 0:
            ret += bit_dat[pos]
            pos -= (pos & -pos)
        return ret

    ans = 0
    for t in T:
        leq = get_sum(t)
        ans += leq
        add(t, 1)

    print(ans)


main()
