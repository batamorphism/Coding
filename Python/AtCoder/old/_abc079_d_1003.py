def main():
    h, w = map(int, input().split())
    r_end = h
    c_end = w
    INF = 10**10
    C = [list(map(int, input().split())) for _ in range(10)]
    # C[i][j] = 数字をiからjに変えるのに必要
    town = [list(map(int, input().split())) for _ in range(r_end)]
    # town[i][j] == -1の場合、数字が書かれていない
    # FW[fr][to] = frからtoへの最短経路であって、frとto以外はk以下の数値しか使わない
    FW = [[INF]*10 for _ in range(10)]
    for fr in range(10):
        for to in range(10):
            FW[fr][to] = C[fr][to]
    for k in range(10):
        for fr in range(10):
            for to in range(10):
                use_k_d = FW[fr][k]+FW[k][to]
                not_k_d = FW[fr][to]
                FW[fr][to] = min(use_k_d, not_k_d)

    ans = 0
    for r in range(r_end):
        for c in range(c_end):
            if town[r][c] == -1:
                continue
            ans += FW[town[r][c]][1]
    print(ans)


main()
