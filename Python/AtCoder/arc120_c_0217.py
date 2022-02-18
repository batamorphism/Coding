from collections import defaultdict
from collections import deque


class BIT:
    def __init__(self, n):
        self.bit_end = n+10
        self.bit_dat = [0] * self.bit_end

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
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(n):
        A[i] += i
        B[i] += i

    if sorted(A) != sorted(B):
        print(-1)
        return

    # Bの登場順毎に、Aをソートする
    order = defaultdict(deque)
    for i, b_i in enumerate(B):
        order[b_i].append(i)

    for i in range(n):
        a_i = A[i]
        A[i] = order[a_i].popleft()

    # Aの転倒数を数える
    bit = BIT(n)
    ans = 0
    for a_i in A:
        # aより大なる数を数える
        total = bit.getsum(n+1)
        leq = bit.getsum(a_i)
        gt = total - leq
        ans += gt
        bit.add(a_i, 1)
    print(ans)


main()
