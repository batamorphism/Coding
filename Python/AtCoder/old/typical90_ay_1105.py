def main():
    n, k, p = map(int, input().split())
    A = list(map(int, input().split()))
    split = n//2
    B, C = A[:split], A[split:]
    cnt_B = [[] for _ in range(n+1)]
    cnt_C = [[] for _ in range(n+1)]

    def set_cnt(cnt_B, B):
        n = len(B)
        ALL = 1 << n
        for bit in range(ALL):
            k, p = 0, 0
            for i in range(n+1):
                if bit >> i & 1:
                    k += 1
                    p += B[i]
            cnt_B[k].append(p)

        for arr in cnt_B:
            arr.sort()

    set_cnt(cnt_B, B)
    set_cnt(cnt_C, C)

    ans = 0
    for k_b in range(n+1):
        b_arr = cnt_B[k_b]
        if not b_arr:
            continue
        for ind_b, p_b in enumerate(b_arr):
            ans_b = 1
            p_c = p-p_b
            k_c = k-k_b
            c_arr = cnt_C[k_c]
            if not c_arr:
                continue
            # c_arr[ind]がp_c以下となる最大のindを求める
            ok = -1
            ng = len(c_arr)
            while ng - ok > 1:
                mid = (ok + ng) // 2
                if c_arr[mid] <= p_c:
                    ok = mid
                else:
                    ng = mid
            ans_c = ok+1
            # 個数は、ind+1個
            # print(ans_b, ans_c, k_b, k_c, p_b, p_c)
            ans += ans_b * ans_c

    print(ans)


main()
