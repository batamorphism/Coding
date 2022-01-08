# 転倒数が0となるような選び方
# a, b についてソートする
# mの選び方のうち、aもbも単調増加となる部分列の最大値
# これは、最長増加部分列を求める問題に帰結する
# i > j := a_i > a_j and b_i > b_j
# i < j := else
INF = float('inf')


class edge:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        if self.a < other.a:
            return True
        elif self.a == other.a:
            return self.b > other.b
        else:
            return False


def main():
    n, m = map(int, input().split())
    AB = []
    for _ in range(m):
        a, b = map(int, input().split())
        AB.append(edge(a, b))
    AB.sort()
    # Aをソートした後のBの、最長増加部分列を求める
    # ただし、Aが同じ場合は、bの重複が許されない為
    # bが大きいほど大きいものとみなす
    B = []
    for ab in AB:
        B.append(ab.b)
    ans = LIS(B)
    print(ans)


def LIS(Arr):
    Arr = [-1] + Arr
    n = len(Arr)
    DP = [INF] * (n + 1)
    DP[0] = -INF
    ret = -INF

    for i, a_i in enumerate(Arr[1:], 1):
        # ab_iより大となる最小のjを探す
        ok = n
        ng = -1
        while ok - ng > 1:
            mid = (ok+ng) // 2
            if DP[mid] >= a_i:
                ok = mid
            else:
                ng = mid
        DP[ok] = a_i
        ret = max(ret, ok)

    return ret


# print(LIS([1, 3, 3, 3, 3]))
main()
