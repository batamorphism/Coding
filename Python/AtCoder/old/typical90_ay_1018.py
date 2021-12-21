def make_cnt_of(B, B_cnt_of, p, k):
    for bit in range(1 << len(B)):
        b_k = 0
        b_p = 0
        for i in range(len(B)):
            if bit >> i & 1:
                b_k += 1
                b_p += B[i]
        if b_p > p:
            continue
        if b_k > k:
            continue
        B_cnt_of[b_k].append(b_p)
    for b_p_list in B_cnt_of:
        b_p_list.sort()


def main():
    n, k, p = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[:n//2]
    C = A[n//2:]
    B_cnt_of = [[] for _ in range(k+1)]
    C_cnt_of = [[] for _ in range(k+1)]
    make_cnt_of(B, B_cnt_of, p, k)
    make_cnt_of(C, C_cnt_of, p, k)
    ans = 0
    for b_k, b_p_list in enumerate(B_cnt_of):
        c_k = k-b_k
        if c_k < 0:
            continue
        c_p_list = C_cnt_of[c_k]
        for b_p in b_p_list:
            c_p = p-b_p
            if c_p < 0:
                continue
            # c_p_list[ok] <= c_pとなる最大のokを探す
            ok = -1
            ng = len(c_p_list)
            while ng-ok > 1:
                mid = (ok+ng)//2
                if c_p_list[mid] <= c_p:
                    ok = mid
                else:
                    ng = mid
            ans += ok+1

    print(ans)


main()
