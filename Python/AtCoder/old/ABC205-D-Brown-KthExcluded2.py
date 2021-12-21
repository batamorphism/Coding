from bisect import bisect


def f(k):
    l, r = 0, 10**19
    while r-l > 1:
        m = l+r >> 1    # l+rの平均
        # aにmを順序を保ったまま挿入し、挿入した箇所…つまり何番目かが返ってくる
        if m - bisect(a, m) < k:
            l = m
        else:
            r = m
    return r


n, q, *z = map(int, open(0).read().split())
a = z[:n]

for k in z[n:]:
    print(f(k))

