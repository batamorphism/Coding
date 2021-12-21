# [0, i)の総和をSUM[i]とする
# [le, ri)の平均は: (SUM[ri]-SUM[le])/(ri-le) >= k
# SUM[ri]-SUM[le] >= k*(ri-le)
# SUM[ri]-k*(ri) >= SUM[le]-k*(le)
# D[i] := SUM[i]-k*iとする
# D[le] <= D[ri]
# となる個数を求める
bit_end = 10**6
bit_dat = [0] * (bit_end + 10)


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


def main():
    n, k = map(int, input().split())
    # 累積和は1-indexed
    A = [0] + [int(input()) for _ in range(n)]
    n += 1
    # 累積和にする
    for i in range(1, n):
        A[i] += A[i-1]
    # kiを引く
    for i in range(n):
        A[i] -= k*i

    # Aを座標圧縮
    zipper_A = {a: i for i, a in enumerate(sorted(list(set(A))))}
    zip_A = [zipper_A[a] for a in A]

    ans = 0
    for a in zip_A:
        ans += getsum(a)
        add(a, 1)

    print(ans)


main()
