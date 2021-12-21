mod = 998244353
rev2 = (mod+1)//2

def main():
    n = int(input())
    A = list(map(int, input().split()))

    # 座標圧縮
    A_zipper = {a: i for i, a in enumerate(sorted(set(A)))}
    A = [A_zipper[a] for a in A]

    # setup bit
    bit_end = n + 10
    bit_data = [0] * bit_end

    def getsum(pos):
        pos += 1
        ret = 0
        while pos > 0:
            ret += bit_data[pos]
            pos -= (pos & -pos)
        return ret

    def add(pos, val):
        pos += 1
        while pos < bit_end:
            bit_data[pos] += val
            pos += (pos & -pos)

    # 各[le, ri]に対して、
    # 2**(ri-le-1)個存在する
    # 2**(ri-le1-1)+2**(ri-le2-1)+...
    # = (2**ri * SUM(-2**(le)) / 2
    ans = 0
    for i, a_i in enumerate(A):
        sum_2_le = getsum(a_i)
        add(a_i, pow(rev2, i, mod))
        ans += pow(2, i, mod) * sum_2_le * rev2
        ans %= mod
    print(ans)


main()
