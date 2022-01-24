def main():
    MOD = 998244353
    n = int(input())
    _ = int(input())
    C = list(map(int, input().split()))
    mask = 0
    for c in C:
        mask += 1 << c

    ALL = 1 << 10

    high_S = 0

    number = [0] + list(map(int, str(n)))
    # DP[deg][S]
    DP = [[0] * ALL for _ in range(len(number))]
    DP_SUM = [[0] * ALL for _ in range(len(number))]
    high = 0
    # 配るDP
    for deg in range(len(number)-1):
        # 1. 新たに追加される1桁の数
        if deg >= 1:
            for new_val in range(1, 10):
                new_S = 1 << new_val
                DP[deg+1][new_S] += 1
                DP_SUM[deg+1][new_S] += new_val
                DP_SUM[deg+1][new_S] %= MOD

        for cur_S in range(ALL):
            # 2. 既存の数に1桁追加
            for new_val in range(10):
                new_S = cur_S | (1 << new_val)
                DP[deg+1][new_S] += DP[deg][cur_S]
                DP[deg+1][new_S] %= MOD
                DP_SUM[deg+1][new_S] += DP_SUM[deg][cur_S]*10 + new_val*DP[deg][cur_S]
                DP_SUM[deg+1][new_S] %= MOD

        # 3. highから生成
        # 3-1. highの末尾に0を追加
        cur_S = high_S
        new_val_end = number[deg+1]
        if new_val_end >= 1:
            if deg >= 1:
                new_val = 0
                new_S = cur_S | (1 << new_val)
                DP[deg+1][new_S] += 1
                DP_SUM[deg+1][new_S] += high*10
                DP_SUM[deg+1][new_S] %= MOD
        # 3-2. highの末尾に1, ..., nex_val_en-d-1を追加
        if new_val_end >= 2:
            for new_val in range(1, new_val_end):
                new_S = cur_S | (1 << new_val)
                DP[deg+1][new_S] += 1
                DP_SUM[deg+1][new_S] += high*10 + new_val
                DP_SUM[deg+1][new_S] %= MOD

        # 4. highを更新
        high *= 10
        high += number[deg+1]
        high %= MOD
        high_S |= 1 << number[deg+1]

    # 5. 0とhighを追加 -> 0は対象外
    last_S = high_S
    DP[len(number)-1][last_S] += 1
    DP_SUM[len(number)-1][last_S] += high

    ans_c = 0
    ans_s = 0
    for S in range(ALL):
        if S & mask == mask:
            # ans_c += DP[len(number)-1][S]
            ans_s += DP_SUM[len(number)-1][S]
            ans_s %= MOD

    print(ans_s)


main()
