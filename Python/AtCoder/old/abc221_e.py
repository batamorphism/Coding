# http://hos.ac/slides/20140319_bit.pdf
class Bit:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def sum(self, ind):
        s = 0
        i = ind
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, ind, x):
        i = ind
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def lower_bound(self, target):
        """
        a_1 + a_2 + ... + a_x >= target となるような
        最小の x を求める(ただし a_i >= 0)
        Args:
            x ([type]): [description]
        """
        if target <= 0:
            return 0
        x = 0
        r = 1  # sizeを超える最小の2のべき乗
        while r < self.size:
            r = r << 1
        len = r
        while len > 0:
            if x+len < self.size and self.tree[x+len]<target:
                target -= self.tree[x+len]
                x += len
            len = len >> 1
        return x+1


def main():
    p = 998244353
    n = int(input())
    A = list(map(int, input().split()))
    bit = Bit(n+10)
    div = pow(2, p-2, p)

    ans = 0
    # Aを座標圧縮
    A_sorted = list(sorted(A))
    A_dict = {a: i for i, a in enumerate(A_sorted)}
    AA = [0]*n
    for i, c in enumerate(A):
        AA[i] = A_dict[c]+1
    A = AA

    for i, a in enumerate(A):
        ans += bit.sum(a)*pow(2, i, p)
        ans = ans % p
        bit.add(a, pow(div, i+1, p))
    print(ans)


main()
