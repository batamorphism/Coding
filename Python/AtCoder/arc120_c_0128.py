from collections import defaultdict


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(n):
        A[i] += i
        B[i] += i

    # AをswapしてBにできるか
    if sorted(A) != sorted(B):
        print(-1)
        return

    # ソートに必要なswapの回数は転倒数
    # Bの要素の登場順に、0, 1, ...で附番していく
    index_of = defaultdict(list)
    for i, b_i in enumerate(B):
        index_of[b_i].append(i)

    A_reorder = [0] * n
    cnt_of = defaultdict(int)
    # Aをindex_ofに従って採番する
    for i, a_i in enumerate(A):
        cnt = cnt_of[a_i]
        ind = index_of[a_i][cnt]
        A_reorder[i] = ind
        cnt_of[a_i] += 1

    # A_recorderの転倒数を数える
    # bit
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
    for i, a_i in enumerate(A_reorder):
        # a_iより大きい数を数える
        # 既にi個の要素を持っているので、a_i以下の数を数えればよい
        gt = i - getsum(a_i)
        ans += gt
        add(a_i, 1)

    print(ans)


main()

