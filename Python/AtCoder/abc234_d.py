# 与えられたもののうち、k番目に大きい値は、BITで求められる
def main():
    n, k = map(int, input().split())
    P = list(map(int, input().split()))

    bit_end = n + 10
    bit_dat = [0] * bit_end

    def add(pos, val):
        pos += 1
        while pos < bit_end:
            bit_dat[pos] += val
            pos += (pos & -pos)

    def getsum(pos):
        ret = 0
        pos += 1
        while pos > 0:
            ret += bit_dat[pos]
            pos -= (pos & -pos)
        return ret

    ans = []
    for i, p_i in enumerate(P):
        if i < k-1:
            # 最初のk要素は無条件に追加
            add(p_i, 1)
        else:
            add(p_i, 1)
            # k番目に大きい値を求める
            # 大きい個数がk個か
            ok = n+1
            ng = 0
            while abs(ng - ok) > 1:
                mid = (ok + ng) // 2
                if getsum(n+1) - getsum(mid) < k:
                    ok = mid
                else:
                    ng = mid
            ans.append(ok)

    print(*ans, sep='\n')


main()
