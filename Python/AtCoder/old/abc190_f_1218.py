# BはAをk個右にシフトさせたもの
# Aを2個くっつけて、しゃくとり法で転倒数を計算していけばよい
from collections import deque


class BIT:
    def __init__(self, n):
        self.bit_end = n+10
        self.bit_dat = [0]*(self.bit_end)

    def add(self, pos, val):
        pos += 1
        while pos < self.bit_end:
            self.bit_dat[pos] += val
            pos += pos & -pos

    def getsum(self, pos):
        pos += 1
        ret = 0
        while pos > 0:
            ret += self.bit_dat[pos]
            pos -= pos & -pos
        return ret


def main():
    # input
    n = int(input())
    A = list(map(int, input().split()))

    # 円環なので二倍
    A += A
    # 転倒数
    bit = BIT(n)
    inv_num = 0
    # しゃくとり法
    que = deque()
    ans = []
    for a in A:
        que.append(a)
        # aより大きいの要素の数だけ、inv_numが増える
        bit.add(a, 1)
        inv_num += len(que) - bit.getsum(a)
        while que and not len(que) <= n:
            rm = que.popleft()
            # rm未満の要素の数だけ、inv_numが減る
            inv_num -= bit.getsum(rm-1)
            bit.add(rm, -1)
        ans.append(inv_num)

    ans = ans[n-1:2*n-1]
    print(*ans, sep='\n')


main()
