def main():
    r_end, c_end = map(int, input().split())
    # cost_of[i][j] = iをjにかえるときのコスト
    cost_of = [list(map(int, input().split())) for _ in range(10)]
    town = [list(map(int, input().split())) for _ in range(r_end)]
    INF = 10**9
    # iをjにかえるときの最小のコスト
    dist_of = [[INF]*10 for _ in range(10)]
    for k in range(10):
        for fr in range(10):
            for to in range(10):
                # frからtoへの経路で、途中でk以下しか使わない場合の最小のコスト
                cost_direct = cost_of[fr][to]
                cost_use_k = dist_of[fr][k]+dist_of[k][to]
                cost_not_k = dist_of[fr][to]
                dist_of[fr][to] = min(cost_use_k, cost_direct, cost_not_k)
    ans = 0
    for r in range(r_end):
        for c in range(c_end):
            if town[r][c] == -1:
                continue
            ans += dist_of[town[r][c]][1]
    print(ans)


main()
