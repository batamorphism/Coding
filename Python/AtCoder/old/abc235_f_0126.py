def main():
    numbers = [0] + list(map(int, input()))
    _ = input()
    C = list(map(int, input().split()))
    mask = 0
    for c in C:
        mask += 1 << c
    del C
    ALL = 1 << 10
    MOD = 998244353

    # 桁DP
    DP = [0]*ALL
    DP_SUM = [0]*ALL
    top = 0
    top_S = 0
    for dgt in range(len(numbers)-1):
        new_DP = [0]*ALL
        new_DP_SUM = [0]*ALL
        # 1. 1桁の数
        if dgt >= 1:
            for val in range(1, 10):
                nex_S = 1 << val
                new_DP[nex_S] += 1
                new_DP_SUM[nex_S] += val

        # 2. 今までの数に10倍してvalを足す
        """ これは遅い
        for cur_S in range(ALL):
            for val in range(10):
        """
        for val in range(10):  # valが先だと早い
            for cur_S in range(ALL):
                nex_S = cur_S | (1 << val)
                new_DP[nex_S] += DP[cur_S]
                new_DP_SUM[nex_S] += DP_SUM[cur_S]*10 + val*DP[cur_S]

        # 3. topを10倍してvalを足す
        if top == 0:
            val_begin = 1
        else:
            val_begin = 0
        val_end = numbers[dgt+1]
        cur_S = top_S
        for val in range(val_begin, val_end):
            nex_S = cur_S | (1 << val)
            new_DP[nex_S] += 1
            new_DP_SUM[nex_S] += top*10 + val

        # 4. 更新
        top = top*10 + numbers[dgt+1]
        top %= MOD
        top_S = top_S | (1 << numbers[dgt+1])
        for S in range(ALL):
            DP[S] = new_DP[S] % MOD
            DP_SUM[S] = new_DP_SUM[S] % MOD

    # 5. 最後の桁
    DP[top_S] += 1
    DP_SUM[top_S] += top

    ans = 0
    for S in range(ALL):
        if S & mask == mask:
            ans += DP_SUM[S]
            ans %= MOD

    print(ans)


main()
