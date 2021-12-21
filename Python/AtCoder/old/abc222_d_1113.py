# DP
# DP[ind][val]  ind番目まで見て、末尾がvalとなる組み合わせ数
# DP[ind][val] = SUM(DP[ind-1][0]+...+DP[ind-1][val])
# ただし、A[ind] <= val <= B[ind]の時に限る
# Binary Indexed Tree
mod = 998244353


class BIT:
    def __init__(self):
        self.bit_end = 3010
        self.data = [0]*(self.bit_end+10)

    def add(self, pos, val):
        pos += 1
        while pos < self.bit_end:
            self.data[pos] += val
            self.data[pos] %= mod
            pos += pos & -pos

    def getsum(self, pos):
        ret = 0
        pos += 1
        while pos > 0:
            ret += self.data[pos]
            ret %= mod
            pos -= pos & -pos
        return ret


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = [0] + A
    B = [0] + B
    n_end = n + 1
    bit_list = [BIT() for _ in range(n_end)]

    bit_list[0].add(0, 1)

    for ind in range(1, n_end):
        for val in range(0, 3001):
            if A[ind] <= val <= B[ind]:
                dp = bit_list[ind-1].getsum(val)
                bit_list[ind].add(val, dp)

    ans = bit_list[n].getsum(3001)
    print(ans)


main()
