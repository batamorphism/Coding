def main():
    n, k = map(int, input().split())
    S_list = []
    for _ in range(n):
        s = input()
        int_list = [c2i(c) for c in s]
        bit = 0
        for i in int_list:
            bit |= 1 << i
        S_list.append(bit)

    # 包除原理
    MOD = 998244353
    ans = 0
    ALL = 1 << n
    for bit in range(1, ALL):
        cnt = 0
        s = -1
        for i in range(n):
            if bit & (1 << i):
                cnt += 1
                s &= S_list[i]
        # sが、bitによる共通部分
        char_cnt = popcount(s)
        # 使える文字の種類数**k通りが答え
        cur_ans = pow(char_cnt, k, MOD)
        # cntが奇数の場合は、加算
        if cnt % 2 == 0:
            cur_ans *= -1
        ans += cur_ans 
        ans %= MOD
    print(ans)


def c2i(c):
    return ord(c) - ord('a')


def popcount(S):
    return bin(S).count('1')


main()
