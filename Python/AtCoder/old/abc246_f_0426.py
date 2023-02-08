MOD = 998244353


def main():
    n, c_cnt = map(int, input().split())
    tw_list = []
    for _ in range(n):
        s = list(input())
        s = [c2i(c) for c in s]
        # 書ける文字の集合に置き換える
        tw = 0
        for c in s:
            tw |= 1 << c
        tw_list.append(tw)
    del s, c

    ans = 0
    S_end = 1 << n
    # 包除原理
    for S in range(1, S_end):
        # type writerからいくつか選んで
        # 何文字書けるか数えていく
        avail_char = -1
        for i in range(n):
            if (S >> i) & 1:
                avail_char &= tw_list[i]
        avail_char_cnt = popcount(avail_char)
        cur_ans = pow(avail_char_cnt, c_cnt, MOD)
        is_even = (popcount(S) % 2 == 0)
        # 包除原理により、偶数の時は引く、奇数の時は足す
        if is_even:
            ans -= cur_ans
        else:
            ans += cur_ans
        ans %= MOD

    print(ans)


def c2i(c):
    return ord(c) - ord('a')


def popcount(x):
    return bin(x).count('1')


main()
