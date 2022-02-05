from collections import deque


class BIT:
    def __init__(self, n, MOD=None):
        self.bit_end = n + 10
        self.bit_dat = [0] * self.bit_end
        self.bit_all = 0
        self.MOD = MOD

    def add(self, pos, val):
        pos += 1
        while pos < self.bit_end:
            self.bit_dat[pos] += val
            if self.MOD:
                self.bit_dat[pos] %= self.MOD
            pos += pos & -pos
        self.bit_all += val
        if self.MOD:
            self.bit_all %= self.MOD

    def get_sum(self, pos):
        pos += 1
        ret = 0
        while pos > 0:
            ret += self.bit_dat[pos]
            pos -= pos & -pos
        if self.MOD:
            ret %= self.MOD
        return ret

    def get_one_val(self, pos):
        ret = self.get_sum(pos) - self.get_sum(pos - 1)
        if self.MOD:
            ret %= self.MOD
        return ret


def main():
    MOD = 10**9 + 7
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    # 座圧
    Zipper_A = {a: i for i, a in enumerate(sorted(list(set(A))))}
    A = [Zipper_A[a] for a in A]

    le_of = [-1]*n
    # le_of[ri]で、[le, ri]のバブルソートの交換回数がk回以下となる最小のindex
    bit_swap = BIT(n)
    # しゃくとり法
    que = deque()
    swap_cnt = 0
    for le in reversed(range(n)):
        a_le = A[le]
        que.append((a_le, le))
        bit_swap.add(a_le, 1)
        lower_a_le = bit_swap.get_sum(a_le-1)
        swap_cnt += lower_a_le
        while que and not swap_cnt <= k:
            a_ri, ri = que.popleft()
            greater_a_ri = bit_swap.bit_all - bit_swap.get_sum(a_ri)
            swap_cnt -= greater_a_ri
            bit_swap.add(a_ri, -1)
            le_of[ri] = le+1

    # 最後まで残ったやつら
    while que:
        a_ri, ri = que.popleft()
        le_of[ri] = 0

    # print(le_of)
    bit_dp = BIT(n+1, MOD)
    bit_dp.add(0, 1)
    for ri_, a_ri in enumerate(A):
        le = le_of[ri_] + 1
        ri = ri_ + 1
        # [le-1, ri-1]の総和を取る
        # ややこしいので、1-indexedにしておく
        dp = bit_dp.get_sum(ri-1) - bit_dp.get_sum(le-2)
        bit_dp.add(ri, dp)

    ans = bit_dp.get_one_val(n)
    print(ans)


main()
