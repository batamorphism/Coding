def main():
    r_end, c_end, n = map(int, input().split())
    rc_list = []
    for _ in range(n):
        r, c, a = map(int, input().split())
        r -= 1
        c -= 1
        rc_list.append((a, r, c))
    rc_list_original = rc_list[:]
    rc_list.sort(reverse=True)

    # 各rに対し、最大の移動回数を返す
    DP_R = [0]*r_end
    DP_C = [0]*c_end
    ans = {}
    pre_a = -1
    batch = set()
    for a, r, c in rc_list:
        if a != pre_a:
            for rr, cc, dp in batch:
                DP_R[rr] = max(dp+1, DP_R[rr])
                DP_C[cc] = max(dp+1, DP_C[cc])
            batch = set()
            pre_a = a
        dp = DP_R[r]
        dp = max(DP_C[c], dp)
        ans[(r, c)] = dp
        batch.add((r, c, dp))

    for _, r, c in rc_list_original:
        print(ans[(r, c)])


main()
