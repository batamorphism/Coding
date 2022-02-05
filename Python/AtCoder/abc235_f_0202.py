def main():
    number = list(map(int, input()))
    m = int(input())
    C = list(map(int, input().split()))
    mask = 0
    for c in C:
        mask |= 1 << c

    ALL = 1 << 10
    MOD = 998244353
    # DP[i][S] := i桁目まで見て、既にSを使っているときの組み合わせ数
    # DP_SUM[i][S] := i桁目まで見て、既にSを使っているときの総和
    # DP = [[0]*ALL for _ in range(len(number)+1)]
    # DP_SUM = [[0]*ALL for _ in range(len(number)+1)]
    DP = [0]*ALL
    DP_SUM = [0]*ALL
    top_val = 0
    top_S = 0
    for cur_dgt in range(len(number)):
        new_DP = [0]*ALL
        new_DP_SUM = [0]*ALL
        nex_dgt = cur_dgt + 1
        # 1. 1桁の数
        if cur_dgt != 0:
            for val in range(1, 10):
                new_DP[1 << val] += 1
                new_DP_SUM[1 << val] += val
        # 2. 既に存在する数の末尾に追加
        for val in range(10):
            for cur_S in range(ALL):
                nex_S = cur_S | (1 << val)
                new_DP[nex_S] += DP[cur_S]
                new_DP_SUM[nex_S] += DP_SUM[cur_S]*10 + val*DP[cur_S]
        # 3. top_valから連鎖
        if cur_dgt == 0:
            nex_val_begin = 1
        else:
            nex_val_begin = 0
        nex_val_end = number[cur_dgt]
        for nex_val in range(nex_val_begin, nex_val_end):
            nex_S = top_S | (1 << nex_val)
            new_DP[nex_S] += 1
            new_DP_SUM[nex_S] += top_val*10 + nex_val
        # top_valを更新
        top_val = top_val*10 + number[cur_dgt]
        top_val %= MOD
        top_S |= 1 << number[cur_dgt]
        for S in range(ALL):
            DP[S] = new_DP[S] % MOD
            DP_SUM[S] = new_DP_SUM[S] % MOD

    # top_valを更新
    DP[top_S] += 1
    DP_SUM[top_S] += top_val

    ans = 0
    for S in range(ALL):
        if S & mask == mask:
            ans += DP_SUM[S]
            ans %= MOD

    print(ans)


main()
