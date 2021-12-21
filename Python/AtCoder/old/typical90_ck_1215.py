from collections import deque
mod = 10**9 + 7


class BIT:
    def __init__(self, n):
        self.bit_end = n + 10
        self.bit_data = [0] * self.bit_end

    def add(self, pos, val):
        val %= mod
        pos += 1
        while pos < self.bit_end:
            self.bit_data[pos] += val
            self.bit_data[pos] %= mod
            pos += pos & -pos

    def getsum(self, pos):
        pos += 1
        ret = 0
        while pos > 0:
            ret += self.bit_data[pos]
            ret %= mod
            pos -= pos & -pos
        return ret


# 1-indexed
def main():
    n, k = map(int, input().split())
    A = [0] + list(map(int, input().split()))

    # 座標圧縮
    A_zipper = {a: i for i, a in enumerate(sorted(set(A)))}
    A = [A_zipper[a] for a in A]

    # f(ri) = [le, ri]で転倒数がk以下となる最小のle
    # しゃくとり法+BIT
    que = deque()
    bit = BIT(n)
    f = [-1] * (n + 1)
    inv_cnt = 0
    for ri, a_ri in enumerate(A[1:], 1):
        que.append((a_ri, ri))
        bit.add(a_ri, 1)
        # a_riが増えたことで、転倒数が増える
        inv_cnt += len(que) - bit.getsum(a_ri)
        while que and not (inv_cnt <= k):
            a_le, le = que.popleft()
            # a_leが消えたことで、転倒数が減る
            inv_cnt -= bit.getsum(a_le-1)
            bit.add(a_le, -1)
        f[ri] = que[0][1]

    # print(f[1:])
    # DP[ri] = DP[ri-1]
    #        + DP[ri-2]
    #     ...+ DP[f(ri)-1]
    # DP[0] = 1
    DP = BIT(n)
    DP.add(0, 1)

    for ri in range(1, n + 1):
        if f[ri] - 2 < 0:
            dp = DP.getsum(ri - 1)
        else:
            dp = DP.getsum(ri - 1) - DP.getsum(f[ri] - 2)
        # print(ri, f[ri], dp)
        DP.add(ri, dp)

    ans = DP.getsum(n) - DP.getsum(n-1)
    ans %= mod
    print(ans)


main()
