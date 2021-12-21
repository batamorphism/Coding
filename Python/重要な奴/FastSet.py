import sys


class FastSet:
    """C++ like set (ordered set) whose elements are limited to integers less than
    about 10 ** 10.

    The number `n` is supposed to be less than about 10 ** 10,
    and the elements added to the set must be less than `n`.

    Reference:
    https://www.dropbox.com/s/1zxohqaxrb87uft/Gifted_Infants_The_University_of_Tokyo___erated_files-job_14.pdf?dl=0
    """

    B = sys.int_info.bits_per_digit

    def __init__(self, n: int) -> None:
        """It creates an ordered set of 0 elements.
        All the elements added to the set must be integers in [0, n).

        Constraints
        -----------

        >   n < 10 ** 10

        Complexity
        ----------

        >   O(n / B), where `B = sys.int_info.bits_per_digit`.
        """
        self.n = n
        self.seg = []
        while True:
            self.seg.append([0] * ((n + self.B - 1) // self.B))
            n = (n + self.B - 1) // self.B
            if n <= 1:
                break
        self.lg = len(self.seg)
        self.size = 0

    def _bsf(self, n):
        "n > 0"
        return ((n & -n) - 1).bit_length()

    def _bsr(self, n):
        "n > 0"
        return n.bit_length() - 1

    def contains(self, i: int) -> bool:
        """It returns whether or not `i` is in the set.

        Complexity
        ----------

        >   O(1)
        """
        if not 0 <= i < self.n:
            return False
        return bool((self.seg[0][i // self.B] >> (i % self.B)) & 1)

    __contains__ = contains

    def add(self, i: int) -> None:
        """It adds `i` to the set.

        Constraints
        -----------

        >   0 <= i < n

        Complexity
        ----------

        >   O(log n)
        """
        assert 0 <= i < self.n
        if i in self:
            return
        self.size += 1
        for h in range(self.lg):
            self.seg[h][i // self.B] |= 1 << (i % self.B)
            i //= self.B

    def discard(self, i: int) -> None:
        """It discards `i` from the set.

        Constraints
        -----------

        >   0 <= i < n

        Complexity
        ----------

        >   O(log n)
        """
        assert 0 <= i < self.n
        if i not in self:
            return
        self.size -= 1
        for h in range(self.lg):
            self.seg[h][i // self.B] &= ~(1 << (i % self.B))
            if self.seg[h][i // self.B]:
                break
            i //= self.B

    def next(self, i: int) -> int:
        """It returns minimum `e` in the set satisfying `i <= e`.
        If such `e` does not exist, it returns `n`.

        Complexity
        ----------

        >   O(log n)
        """
        if self.n <= i:
            return self.n
        if i < 0:
            i = 0
        for h in range(self.lg):
            if i // self.B == len(self.seg[h]):
                break
            d = self.seg[h][i // self.B] >> (i % self.B)
            if d == 0:
                i = i // self.B + 1
                continue
            i += self._bsf(d)
            for g in reversed(range(h)):
                i *= self.B
                i += self._bsf(self.seg[g][i // self.B])
            return i
        return self.n

    def prev(self, i: int) -> int:
        """It returns maximum `e` in the set satisfying `e < i`.
        If such `e` does not exist, it returns -1.


        Complexity
        ----------

        >   O(log n)
        """
        if i <= 0:
            return -1
        if self.n <= i:
            i = self.n
        i -= 1
        for h in range(self.lg):
            if i == -1:
                break
            s = ((-i-1) % self.B)
            d = (self.seg[h][i // self.B] & ((1 << (self.B - s)) - 1))
            if d == 0:
                i = i // self.B - 1
                continue
            i += self._bsr(d) + s - (self.B - 1)
            for g in reversed(range(h)):
                i *= self.B
                i += self._bsr(self.seg[g][i // self.B])
            return i
        return -1

    def minimum(self) -> int:
        """It returns the minimum element in the set.
        If the set has no elements, it returns `n`.

        Complexity
        ----------

        >   O(log n)
        """
        return self.next(0)

    def maximum(self) -> int:
        """It returns the maximum element in the set.
        If the set has no elements, it returns -1.

        Complexity
        ----------

        >   O(log n)
        """
        return self.prev(self.n)

    def __len__(self) -> int:
        return self.size

    def __bool__(self) -> bool:
        return bool(len(self))

    def __iter__(self) -> None:
        e = -1
        while True:
            e = self.next(e + 1)
            if e == self.n:
                break
            yield e

    def __repr__(self):
        return '{0}({1!r}, n={2})'.format(type(self).__name__,
                                          list(self),
                                          self.n)


if __name__ == "__main__":
    import sys
    import time
    time.sleep(1)
    input = sys.stdin.readline

    L, Q = map(int, input().split())
    cxs = [tuple(map(int, input().split())) for _ in range(Q)]

    fs = FastSet(10 ** 9 + 10)
    fs.add(0)
    fs.add(L)
    L in fs
    for c, x in cxs:
        if c == 1:
            fs.add(x)
        else:
            p = fs.prev(x)
            n = fs.next(x)
            print(n - p)
