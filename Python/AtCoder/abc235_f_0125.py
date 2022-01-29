# 桁DP
def main():
    n = input()
    _ = int(input())
    C = list(map(int, input().split()))
    MOD = 998244353
    mask = 0
    for c in C:
        mask += 1 << c
    del C

    number = [0] + list(map(int, n))
    high = 0
    high_S = 0
    ALL = 1 << 10
    DP = [0] * ALL
    DP_SUM = [0] * ALL
    new_DP = [0] * ALL
    new_DP_SUM = [0] * ALL

    # 桁DPは配るDP
    for deg in range(len(number)-1):
        new_DP = [0] * ALL
        new_DP_SUM = [0] * ALL

        # 1. 新たに始まる1桁の数1～9
        if deg >= 1:
            cur_S = 0
            for val in range(1, 10):
                nex_S = cur_S | (1 << val)
                new_DP[nex_S] += 1
                new_DP_SUM[nex_S] += val

        # 2. 既に確定している数に0～10を追加
        for cur_S in range(ALL):
            for val in range(10):
                nex_S = cur_S | (1 << val)
                new_DP[nex_S] += DP[cur_S]
                new_DP_SUM[nex_S] += DP_SUM[cur_S]*10 + val*DP[cur_S]

        # 3. highから始まる数high*10+0～high*10+(val_end-1)
        if deg == 0:
            val_begin = 1  # 初回は0から始めると先頭桁が0の数字になってしまうので除外
        else:
            val_begin = 0
        val_end = number[deg+1]
        cur_S = high_S
        for val in range(val_begin, val_end):
            nex_S = cur_S | (1 << val)
            new_DP[nex_S] += 1
            new_DP_SUM[nex_S] += (high*10 + val) % MOD
            new_DP_SUM[nex_S] %= MOD

        # 更新
        high = (high * 10 + number[deg+1]) % MOD
        high_S |= (1 << number[deg+1])
        for S in range(ALL):
            DP[S] = new_DP[S]
            DP_SUM[S] = new_DP_SUM[S]
            DP[S] %= MOD
            DP_SUM[S] %= MOD

    # highそのものの更新
    DP[high_S] += 1
    DP_SUM[high_S] += high
    DP_SUM[high_S] %= MOD

    ans_s = 0
    for S in range(ALL):
        if S & mask == mask:
            ans_s += DP_SUM[S]
            ans_s %= MOD

    print(ans_s)


main()
