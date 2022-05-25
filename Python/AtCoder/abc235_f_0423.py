def main():
    MOD = 998244353

    n = int(input())
    m = int(input())
    C = list(map(int, input().split()))

    mask = 0
    for c in C:
        mask |= 1 << c

    # 桁DP
    # DP[S] = Sを全て含むようなすべての和
    S_end = 1 << 10  # 0, ....,9からなる数字の集合
    DP = [0]*S_end  # 合計がいくつか
    cntDP = [0]*S_end  # 何通りあるか

    n_list = list(map(int, str(n)))
    top_val = 0
    top_S = 0

    for i, n_i in enumerate(n_list):
        new_DP = [0]*S_end
        new_cntDP = [0]*S_end
        # 1. 既にある数の末尾に0～9を追加する
        if i == 0:
            v_begin = 1  # 初回は、0を追加してはならない
        else:
            v_begin = 0
        v_end = 10
        for v in range(v_begin, v_end):
            for cur_S in range(S_end):
                nex_S = cur_S | (1 << v)
                new_cntDP[nex_S] += cntDP[cur_S]
                new_DP[nex_S] += DP[cur_S]*10 + v*cntDP[cur_S]

        # 2. 新たに1桁の数字を追加する
        if i != 0:  # 初回は、1桁の数値を追加してはならない
            for v in range(1, 10):
                nex_S = 1 << v
                new_DP[nex_S] += v
                new_cntDP[nex_S] += 1

        # 3. top_valから連鎖
        if i == 0:
            v_begin = 1
        else:
            v_begin = 0
        v_end = n_i
        for v in range(v_begin, v_end):
            # top_val * 10 + vを追加する
            nex_S = top_S | (1 << v)
            new_DP[nex_S] += top_val*10 + v
            new_cntDP[nex_S] += 1

        # 4. 更新
        top_val = top_val * 10 + n_i
        top_val %= MOD
        top_S |= 1 << n_i
        for S in range(S_end):
            DP[S] = new_DP[S] % MOD
            cntDP[S] = new_cntDP[S] % MOD

    # 5. 最後に、top_valを追加する
    DP[top_S] += top_val
    ans = 0
    for S in range(S_end):
        if S & mask == mask:
            ans += DP[S]
            ans %= MOD

    print(ans)


main()
