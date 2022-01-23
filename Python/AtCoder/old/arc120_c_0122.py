from collections import defaultdict


# Aに+iする操作を考える
# 問題で与えられたAへの操作は、A'を並び替える操作と対応する
# すなわち
# A  -> B :問題文中のswap
# |     |
# A' -> B' :通常のswap
# は可換
# したがって、A', B'の並び替えに必要な回数を求めればよい
def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(n):
        A[i] += i
        B[i] += i

    # first check
    if sorted(A) != sorted(B):
        print(-1)
        return

    # AをBにソートする
    # iとb_iを対応付ける
    # a_i == b_jの場合、a_iをjに変える
    zipper = defaultdict(list)
    for i, b_i in enumerate(B):
        zipper[b_i].append(i)
    for li in zipper.values():
        li.sort()

    cnt_of = defaultdict(int)
    new_A = [-1] * n
    for i, a_i in enumerate(A):
        cnt = cnt_of[a_i]
        new_A[i] = zipper[a_i][cnt]
        cnt_of[a_i] += 1
    A = new_A

    # setup bit
    bit_end = n + 10
    bit_dat = [0] * bit_end

    def add(pos, val):
        pos += 1
        while pos < bit_end:
            bit_dat[pos] += val
            pos += (pos & -pos)

    def getsum(pos):
        pos += 1
        ret = 0
        while pos > 0:
            ret += bit_dat[pos]
            pos -= (pos & -pos)
        return ret

    ans = 0
    for i, a_i in enumerate(A):
        # 今まで出てきた要素のうち、aより大の物を数える
        smaller = getsum(a_i)
        greater = i - smaller
        ans += greater
        add(a_i, 1)

    print(ans)


main()
