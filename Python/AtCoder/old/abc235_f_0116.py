def main():
    max_val = list(map(int, input()))
    _ = int(input())
    C = list(map(int, input().split()))
    MOD = 998244353

    mask = 0
    for c in C:
        mask += 1 << c

    # max_val以下で、今まで使った数字をSとした場合の
    # 組み合わせ数と、総和
    # 桁DPは、次の3つから遷移する
    # 今まで確定させた数字
    # 新たにi桁目から始まる数値
    # max_valと同じ値が続く数
    top_val = 0
    top_val_S = 0
    ALL = 1024
    DP_c = [0]*ALL
    DP_s = [0]*ALL
    for i, v_i in enumerate(max_val):
        new_DP_c = [0]*ALL
        new_DP_s = [0]*ALL
        # 既に確定させてある数値の右端にdをくっつける
        for S in range(1, ALL):
            for d in range(10):
                new_S = S | (1 << d)
                new_DP_c[new_S] += DP_c[S]
                # 1桁あがるので10倍、下の桁はdだけ追加
                new_DP_s[new_S] += DP_s[S]*10 + DP_c[S]*d

        # 新たにi桁目から始まる数値
        if i != 0:
            # i == 0の時は、top_valロジックに落ちる
            for d in range(1, 10):
                new_S = 1 << d
                new_DP_c[new_S] += 1
                new_DP_s[new_S] += d

        # top_valから使う
        if i == 0:
            st = 1
        else:
            st = 0
        for d in range(st, v_i):
            new_S = top_val_S | (1 << d)
            new_DP_c[new_S] += 1
            new_DP_s[new_S] += top_val * 10 + d

        top_val = (top_val * 10 + v_i) % MOD
        top_val_S |= 1 << v_i
        for S in range(1, ALL):
            DP_c[S] = new_DP_c[S] % MOD
            DP_s[S] = new_DP_s[S] % MOD

    # 最後の値
    DP_s[top_val_S] += top_val

    ans = 0
    for S, val in enumerate(DP_s):
        if S & mask == mask:
            ans += val
            ans %= MOD
            c = DP_c[S]

    print(ans)


main()
