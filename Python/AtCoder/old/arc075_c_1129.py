import sys
sys.setrecursionlimit(10**6)
# 累積和は1-indexed
# S[i] = A[1]+...+A[i]とする
# S[ri]-S[le] = A[le+1] + ... + A[ri]
# (S[ri]-S[le])/(ri-le) = le+1, ..., riの平均
# (S[ri]-S[le])/(ri-le) >= k (0 <= le < ri <= n)
# (S[ri]-S[le]) >= k*ri-k*le
# S[ri]-k*ri >= S[le]-k*le (le < ri)
# B[i] = S[i]-k*iとして
# B[le] <= B[ri] (0 <= le < ri <= n)を満たすle, riの組み合わせ数を求めればよい
def main():
    n_max, k = map(int, input().split())

    A = [0] + [int(input()) for _ in range(n_max)]
    # 累積和にする
    for i in range(1, n_max+1):
        A[i] += A[i-1]

    for i in range(n_max+1):
        A[i] -= k*i

    # 座圧
    A_zipper = {a: i for i, a in enumerate(sorted(list(set(A))))}
    A = [A_zipper[a] for a in A]

    ans = 0
    # print(A)
    for ri in range(n_max+1):
        a_ri = A[ri]
        ans += getsum(a_ri)
        add(a_ri, 1)

    print(ans)


# setup bit
bit_end = 2*10**5+10
bit_dat = [0]*(bit_end+1)


def add(pos, val):
    pos += 1
    while pos < bit_end:
        bit_dat[pos] += val
        pos += pos & -pos


def getsum(pos):
    pos += 1
    ret = 0
    while pos > 0:
        ret += bit_dat[pos]
        pos -= pos & -pos
    return ret


main()
