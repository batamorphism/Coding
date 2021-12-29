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

# 使用例
bit = Bit(10)     # 要素数を与えてインスタンス化
bit.add(2, 10)    # a2に10を加える
bit.add(5, 5)     # a5に 5を加える
print(bit.sum(3)) # a1～a3の合計を返す => 10
print(bit.sum(6)) # a1～a6の合計を返す => 15
print(bit.lower_bound(13))  # a1+...が13を超えるのは、a5まで足して15になった時=>5
bit.add(3, -6)    # a3に-6を加える
print(bit.sum(6)) # a1～a6の合計を返す => 9
print(bit.sum(6) - bit.sum(3))  # a4～a6の合計 => 5

