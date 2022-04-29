# 各a_iは選ぶか選ばないか（xorは2回やる意味はない)
def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = sum(A)

    # 総和はO(N)で間に合わないので、bit毎に管理する
    bit_cnt = [0] * 31
    for a_i in A:
        for bit in range(31):
            if (a_i >> bit) & 1:
                bit_cnt[bit] += 1

    # 各xに対し、xorを取る->bit_cntをx-bit_cntで更新
    for a_i in A:
        new_bit_cnt = bit_cnt[:]
        for bit in range(31):
            if (a_i >> bit) & 1:
                new_bit_cnt[bit] = n-new_bit_cnt[bit]
        cur_ans = calc_sum(new_bit_cnt)
        ans = max(ans, cur_ans)

    print(ans)


def calc_sum(bit_cnt):
    ret = 0
    for i, cnt in enumerate(bit_cnt):
        ret += (1 << i) * cnt
    return ret


main()
