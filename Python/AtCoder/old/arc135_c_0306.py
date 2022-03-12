# どれか一個だけxorしたのと同じ
# 各bitに、1がいくつあるか


def main():
    n = int(input())
    A = list(map(int, input().split()))
    bit_cnt_of = [0] * 31

    for a in A:
        for bit in range(31):
            if a >> bit & 1:
                bit_cnt_of[bit] += 1

    ans = sum(A)

    # xorを一回やると
    # 各桁について、a_iのbitが1の場合、bit_cnt_ofがn-cntになる
    master_bit_cnt_of = bit_cnt_of[:]
    for a in A:
        bit_cnt_of = master_bit_cnt_of[:]
        for bit in range(31):
            if a >> bit & 1:
                bit_cnt_of[bit] = n-bit_cnt_of[bit]
        pre_ans = calc_ans(bit_cnt_of)
        ans = max(pre_ans, ans)
    print(ans)


def calc_ans(bit_cnt_of):
    ret = 0
    for i, cnt in enumerate(bit_cnt_of):
        ret += cnt * 2**i
    return ret


main()
